import requests
from bs4 import BeautifulSoup

link = 'http://bianca.com/'
requisicao = requests.get(link)
print(requisicao)
# print(requisicao.text)
site = BeautifulSoup(requisicao.text,"html.parser")
# print(site.prettify())

# print(site.title)
titulo = site.find_all("title")
corpo = site.find_all("h1")
print("titulo: ",titulo)
print("corpo: ",corpo)
