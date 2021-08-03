from bs4 import BeautifulSoup
import requests

def get_noticias(url, classe_noticia, classe_titulo, classe_subtitulo):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    noticias = soup.find_all(class_=classe_noticia)
    lista_noticias = []
    for noticia in noticias:
        titulo = noticia.find(class_=classe_titulo)
        if titulo is None:
            continue
        subtitulo = noticia.find(class_=classe_subtitulo)
        noticia = dict()
        noticia["titulo"] = titulo.contents[0]
        if subtitulo is not None:
            noticia["subtitulo"] = subtitulo.contents[0]
        lista_noticias.append(noticia)
    return lista_noticias
