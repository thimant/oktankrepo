FROM python:3.8-slim-buster
USER root

WORKDIR /code

COPY requirements.txt /code/requirements.txt 
RUN pip3 install -r requirements.txt
COPY app.py /code/app.py

COPY ./templates /code/templates
RUN chgrp -R 0 /code && \
    chmod -R g=u /code

RUN ls
EXPOSE 8080
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p=8080"]
