# Use an official Python runtime as a parent image
FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

ENV FLASK_APP main.py

EXPOSE 5000

CMD ["python", "main.py"]