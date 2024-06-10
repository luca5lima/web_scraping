import requests
from bs4 import BeautifulSoup

link = 'http://bianca.com/'

try:
    requisicao = requests.get(link)
    requisicao.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

    site = BeautifulSoup(requisicao.text, "html.parser")
    
    titulos = site.find_all("title")
    corpos = site.find_all("h1")
    
    for titulo in titulos:
        print("Titulo:", titulo.get_text())
    
    for corpo in corpos:
        print("Corpo:", corpo.get_text())

except requests.exceptions.RequestException as e:
    print(f"Erro na solicitação HTTP: {e}")