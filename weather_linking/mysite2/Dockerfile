FROM python:3.7.9-stretch

WORKDIR /mydjango

RUN apt-get update
RUN apt-get install -y vim
RUN pip install django
RUN pip install mysqlclient

COPY bookmark /mydjango/bookmark
COPY mysite2 /mydjango/mysite2
COPY db.sqlite3 /mydjango/db.sqlite3
COPY manage.py /mydjango/manage.py


EXPOSE 8000
EXPOSE 9000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]