FROM python:3.7.9-stretch

RUN pip install django
RUN pip install mysqlclient
RUN pip install requests

ARG PROJECT_DIR=/weather_linking

COPY . ${PROJECT_DIR}
WORKDIR /weather_linking

EXPOSE 8800
EXPOSE 13306

RUN echo "PWD is $PWD"

CMD ["python","manage.py","runserver","0.0.0.0:8000"]