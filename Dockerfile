FROM python:3.9-alpine

RUN mkdir /g1scraper
WORKDIR /g1scraper
ADD requirements.txt /g1scraper
RUN apk update --no-cache && apk upgrade --available --no-cache && \
    apk add --no-cache gcc cargo python3-dev musl-dev openssl-dev libffi-dev libxml2-dev libxslt-dev && \
    python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt && \
    apk del gcc cargo python3-dev musl-dev openssl-dev libffi-dev libxml2-dev libxslt-dev
ADD . /g1scraper

CMD ["gunicorn", "-w4", "-b0.0.0.0:8080", "g1scraper.app:app"]
