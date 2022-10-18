from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<USERNAME>:<PASSWORD>@<RDSENDPOINT>/<DBNAME>?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:mypassword@database-oktank-tobe.csqkr4unxyxx.us-east-1.rds.amazonaws.com/oktankdb?charset=utf8mb4'

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   enem = db.Column(db.String(50))  
   email = db.Column(db.String(200))
   gender = db.Column(db.String(10))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
