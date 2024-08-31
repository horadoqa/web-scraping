# pip install requests bs4
# pip install beautifulsoup4

# Importando as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup

# Definindo a URL da página que queremos raspar
url = 'https://g1.globo.com/'

# Realizando a requisição HTTP para obter o conteúdo da página
resposta = requests.get(url)

# Criando um objeto BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(resposta.text, 'html.parser')

# Encontrando todos os elementos que contêm o título das notícias
titulos_noticias = soup.find_all('a', {'class': 'feed-post-link'})

# Exibindo os títulos das notícias
for titulo in titulos_noticias:
    print(titulo.text.strip())