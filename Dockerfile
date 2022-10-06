FROM python:3.8-slim-buster
USER root

WORKDIR /code

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt

COPY ./templates /code/templates
COPY ./app /code/app
RUN chgrp -R 0 /code && \
    chmod -R g=u /code

EXPOSE 8080
CMD ["python3", "--host", "0.0.0.0", "--port", "8080"]
