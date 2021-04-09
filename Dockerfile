FROM python:latest
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
ADD . /app/
RUN cd /app && python3 manage.py migrate

