FROM python:3.7.9-stretch

WORKDIR /weather_docker

RUN pip install django
RUN pip install mysqlclient
RUN pip install requests

EXPOSE 8800

CMD ["python","manage.py","runserver","0.0.0.0:8800"]