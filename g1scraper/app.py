"""App do g1scraper.

Para executar app via flask (nao recomendado em producao):
$ flask run --host=0.0.0.0

Ou, ainda, com o server gunicorn:
$ gunicorn g1scraper.app:app
"""
from flask import Flask, jsonify

from g1scraper.scrap import get_noticias

app = Flask(__name__)

@app.route("/noticias/geral")
def noticias_geral():
    return jsonify(get_noticias("https://g1.globo.com/"))

@app.route("/noticias/esporte")
def noticias_esporte():
    return jsonify(get_noticias("https://ge.globo.com/"))
