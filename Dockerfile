FROM python:3.8
WORKDIR /usr/src/app

COPY . .
RUN pip install flask

EXPOSE 80

CMD [ "python3", "app.py" ]
