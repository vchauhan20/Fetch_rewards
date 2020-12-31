FROM python:alpine3.7
RUN mkdir /app
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
