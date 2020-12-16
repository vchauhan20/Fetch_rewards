FROM python:alpine:latest
RUN apk add --no cache python3-dev \ && pip3 install --upgarde pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
