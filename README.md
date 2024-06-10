# Web Scraping com Python

Este projeto demonstra como realizar web scraping utilizando Python, `requests` e `BeautifulSoup`. O objetivo é acessar uma página web, extrair o título da página e todos os cabeçalhos `<h1>` presentes nela.

## Requisitos

- Python 3.x
- Bibliotecas `requests` e `BeautifulSoup`

Para instalar as bibliotecas necessárias, execute:
```bash
pip install requests beautifulsoup4
```

## Explicação do Código
### 1. Importação das Bibliotecas:

`requests` é usado para fazer solicitações HTTP.

`BeautifulSoup` do `bs4` é usado para analisar o HTML da resposta.
Definição da URL do Site:

### 2. Definição da URL do Site:

```python
link = 'http://bianca.com/'
```
Define a URL da página que queremos acessar.

### 3. Fazendo a Solicitação HTTP:
```python
requisicao = requests.get(link)
requisicao.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
```

`requests.get(link)` envia uma solicitação HTTP GET para a URL especificada e armazena a resposta na variável `requisicao`.

`raise_for_status()` lança uma exceção se a solicitação não for bem-sucedida (código de status diferente de 200).

### 4. Analisando o Conteúdo HTML:
```python
site = BeautifulSoup(requisicao.text, "html.parser")
```

`BeautifulSoup(requisicao.text, "html.parser")` analisa o conteúdo HTML da resposta usando o parser HTML padrão do BeautifulSoup.

### 5. Extraindo Elementos Específicos:
```python
titulos = site.find_all("title")
corpos = site.find_all("h1")
```

`site.find_all("title")` encontra todos os elementos `<title>` na página e os armazena na variável `titulos`.

`site.find_all("h1")` encontra todos os elementos `<h1>` na página e os armazena na variável `corpos`.

### 6. Imprimindo os Resultados:

```python
for titulo in titulos:
    print("Titulo:", titulo.get_text())

for corpo in corpos:
    print("Corpo:", corpo.get_text())
```

Itera sobre os elementos encontrados e imprime o texto contido em cada um.

### 7. Tratamento de Erros:

```python
except requests.exceptions.RequestException as e:
    print(f"Erro na solicitação HTTP: {e}")

```

Captura exceções que podem ocorrer durante a solicitação HTTP e imprime uma mensagem de erro.

### Raciocínio Resumido
- Importar bibliotecas.
- Definir a URL.
- Fazer a solicitação HTTP.
- Verificar se a solicitação foi bem-sucedida.
- Analisar o conteúdo HTML.
- Extrair elementos `<title>` e `<h1>`.
- Imprimir os resultados.
- Tratar erros de solicitação HTTP.

### Executando o Código

Basta copiar o código acima e colá-lo em um script Python. Execute o script para ver os resultados da extração de dados.
```bash
python seu_script.py
```