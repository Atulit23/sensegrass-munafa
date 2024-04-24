FROM python:3.10.11 AS BASE

RUN pip install --no-cache-dir --upgrade pip

RUN pip install rasa==3.6.19

WORKDIR /app
COPY . .

# RUN rasa train

USER 1001

ENTRYPOINT ["rasa"]

CMD ["run", "--enable-api", "--port", "8080"]
# CMD ["rasa", "run", "actions", "--actions", "actions"]

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml