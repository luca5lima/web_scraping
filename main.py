import requests
from bs4 import BeautifulSoup

link = 'http://bianca.com/'
requisicao = requests.get(link)
print(requisicao)
# print(requisicao.text)
if requisicao.status_code == 200:
    # Analisa o conteúdo HTML da página
    site = BeautifulSoup(requisicao.text, "html.parser")
    
    titulo = site.find_all("title")
    corpo = site.find_all("h1")
    
    print("titulo: ", titulo)
    print("corpo: ", corpo)
else:
    print("Falha na requisição, status code:", requisicao.status_code)