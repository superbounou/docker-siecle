FROM alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

COPY . /app
COPY crontab.dist /app/crontab

RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt

WORKDIR /app

CMD ["/env/bin/python", "siecle.py","scheduler","start"]
