FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY app/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app/. /usr/src/app

EXPOSE 5000

CMD [ "python", "./app.py" ]
