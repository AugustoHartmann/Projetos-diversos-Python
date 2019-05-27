import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
lista = []
entrada = input("Insira o termo de pesquisa: ")
entrada2 = entrada.replace(' ', '%20')
entrada3 =  normalize('NFKD', entrada2).encode('ASCII', 'ignore').decode('ASCII')
pagina = requests.get("https://www.dicio.com.br/"+entrada3+"/")
soup = BeautifulSoup(pagina.content, 'html.parser')
for i in range(0,1):
    conteudo = soup.find("p").get_text()
    lista.append(conteudo)
print(lista)
