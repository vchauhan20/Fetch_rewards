FROM python:alpine3.7
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
EXPOSE $PORT
RUN pip install -r requirements.txt
CMD exec gunicorn app.py
