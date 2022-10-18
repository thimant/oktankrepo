from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<USERNAME>:<PASSWORD>@<RDSENDPOINT>/<DBNAME>?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:mypassword@db.oktankprem.8329.p1.openshiftapps.com/oktankdb?charset=utf8mb4'

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   enem = db.Column(db.String(50))  
   email = db.Column(db.String(200))
   gender = db.Column(db.String(10))

def __init__(self, name, enem, email,gender):
   self.name = name
   self.enem = enem
   self.email = email
   self.gender = gender

@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )
   
@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['enem'] or not request.form['email']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(name=request.form['name'], enem=request.form['enem'],
            email=request.form['email'], gender=request.form['gender'])
         
         db.session.add(student)
         db.session.commit()
         
         
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')
