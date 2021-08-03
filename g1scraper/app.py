from flask import Flask, jsonify

from g1scraper.scrap import get_noticias

app = Flask(__name__)

@app.route("/noticias/geral")
def noticias_geral():
    return jsonify(get_noticias(
        "https://g1.globo.com/",
        "feed-post-body",
        "feed-post-link",
        "feed-post-body-resumo")
    )

@app.route("/noticias/esporte")
def noticias_esporte():
    return jsonify(get_noticias(
        "https://ge.globo.com/",
        "feed-post-body",
        "feed-post-link",
        "feed-post-body-resumo")
    )
