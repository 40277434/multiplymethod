FROM python:3.8
WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python3", "app.py" ]
