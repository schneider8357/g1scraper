FROM python:3.9-alpine

ADD . /g1scraper
WORKDIR /g1scraper

RUN apk add --no-cache gcc cargo python3-dev musl-dev openssl-dev libffi-dev libxml2-dev libxslt-dev
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
CMD ["gunicorn", "-w4", "-b0.0.0.0:8080", "g1scraper.app:app"]
