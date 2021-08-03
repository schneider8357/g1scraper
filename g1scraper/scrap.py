"""Funcoes de scraping."""
import collections
import json

from bs4 import BeautifulSoup
import requests


def get_closing_bracket(string, indice_inicio):
    """Retorna o indice da '}' correspondente a '{' no indice recebido."""
    if string[indice_inicio] != '{':
        raise ValueError("String invalida")
    deque = collections.deque()
    for atual in range(indice_inicio, len(string)):
        if string[atual] == '}' and string[atual-1] != '\\':
            deque.popleft()
        elif string[atual] == '{' and string[atual-1] != '\\':
            deque.append(string[indice_inicio])
        if not deque:
            return atual # O '}' correpondente foi encontrado
    raise ValueError("String invalida")

def get_noticias(url):
    """Retorna as noticias com titulo e subtitulo em uma lista."""
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    lista_noticias = []

    # Buscar noticias em html
    for noticia in soup.find_all(class_="feed-post-body"):
        titulo = noticia.find(class_="feed-post-link")
        if titulo is None or titulo.contents is None:
            continue
        subtitulo = noticia.find(class_="feed-post-body-resumo")
        noticia = dict(titulo=titulo.contents[0], subtitulo=None)
        if subtitulo is not None:
            noticia["subtitulo"] = subtitulo.contents[0]
        lista_noticias.append(noticia)
    
    # Buscar noticias no JSON dentro do JS da pagina
    feed = str(soup.find(class_="fore-posts-setted"))
    indice_chave = feed.find('{"') # O JSON inicia usualmente em "config"
    json_feed = feed[indice_chave : get_closing_bracket(feed, indice_chave)+1]
    dict_feed = json.loads(json_feed)
    for noticia in dict_feed["forePosts"] + dict_feed["items"]:
        if noticia["type"] in ("materia", "cobertura"):
            lista_noticias.append(
                {
                    "titulo": noticia["content"]["title"], 
                    "subtitulo": noticia["content"].get("summary")
                }
            )
    return lista_noticias
