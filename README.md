# g1scraper

Biblioteca que busca as notícias da página inicial dos portais G1 e GE utilizando web scraping.

O `g1scraper` utiliza a biblioteca beautifulsoup4, disponível na PyPI, para realizar o scraping. A biblioteca Flask é utilizada para a aplicação web que serve como API do `g1scraper`.

## Execução com docker

A forma mais simples de executar o `g1scraper` é com a [imagem docker](https://hub.docker.com/repository/docker/schneider8357/g1scraper):

 ```bash
 docker run -p8080:8080 --rm schneider8357/g1scraper
 ```

## Instalação

Para instalar o `g1scraper` localmente, é preciso primeiramente clonar o repositório:
```bash
git clone https://github.com/schneider8357/g1scraper
cd g1scraper
```


E instalar as dependências:
```bash
pip install -r requirements.txt
```

## Execução

Uma vez instalado, para iniciar o `g1scraper` pode-se utilizar o `gunicorn`:

```bash
gunicorn -w 4 -b 0.0.0.0:8080 g1scraper.app:app
```

A quantidade de workers pode ser alterada com a opção `-w`, bem como o host e a porta com a opção `-b`.

## Uso

Para buscar as notícias da página inicial do site `g1.globo.com`, utilize o endpoint `/noticias/geral`:
```bash
curl http://0.0.0.0:8080/noticias/geral
```

Já para buscar as notícias da página inicial do site `ge.globo.com`, utilize o endpoint `/noticias/esporte`:
```bash
curl http://0.0.0.0:8080/noticias/esporte
```
