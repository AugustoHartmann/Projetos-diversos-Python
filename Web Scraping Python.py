import requests
from bs4 import BeautifulSoup

pagina = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
pagina
pagina.status_code
pagina.content
bs = BeautifulSoup(pagina.content, 'html.parser')
print(bs.prettify())
list(bs.children)
