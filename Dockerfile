FROM python:3.9-alpine
USER root

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

COPY ./templates /code/templates
COPY ./app /code/app
RUN chgrp -R 0 /code && \
    chmod -R g=u /code

ENV FILES_BASEPATH=/tmp

EXPOSE 8080
ENTRYPOINT ["/sbin/run.sh"]
CMD ["python app.py", "--host", "0.0.0.0", "--port", "8080"]
