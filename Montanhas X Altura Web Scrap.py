import requests
from bs4 import BeautifulSoup
montanhas = {}
pagina = requests.get("https://en.wikipedia.org/wiki/List_of_mountains_by_elevation")
pagina.content
soup = BeautifulSoup(pagina.content, 'html.parser')
#print(soup.prettify())
html = list(soup.children)[2]
body = list(html.children)[3]
i = 0
for a in range(0,125):
    nomes = soup.find_all('td')[i].get_text()
    alturam = soup.find_all('td')[i+1].get_text()
    alturap = soup.find_all('td')[i+2].get_text()
    montanhas[nomes] = [alturam, alturap]
    i = i + 5
#print(montanhas)
print("Lista das montanhas e suas respectivas alturas em metros e em pés...")
print("")
for nomes in montanhas:
    print("Nome: ",nomes," Altura em metros",montanhas[nomes][0]," Altura em pés",montanhas[nomes][1])
