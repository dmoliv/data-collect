# %%
import requests
from bs4 import BeautifulSoup

url = 'https://www.residentevildatabase.com/personagens/ada-wong/'
resp = requests.get(url)

# %%
resp.status_code

# %%
soup = BeautifulSoup(resp.text)
soup

# %%
div_page = soup.find('div', class_ = 'td-page-content')

# %%
paragrafo = div_page.find_all('p')[1] #filtrando pelo paragrafo na posição 1

# %%
ems = paragrafo.find_all('em') #filtrando ainda mais os elementos

# %%
#transformando os dados em um dicionario chave/valor usando o : como split
data = {}
for i in ems:
    chave, valor = i.text.split(':')
    chave = chave.strip(' ') #strip remove o espaço
    data[chave] = valor.strip(' ')
data

# %%
#acessando o tipo sanguineo do personagem
data['Tipo sanguíneo']

# %%

#procurando pelas aparições em outros jogos
div_page2 = (soup.find('div', class_ = 'td-page-content')
                .find('h4')
                .find_next()
                .find_all('li'))
#o find procura pelo primeiro elemento e o find_all procura tudo após o elemento anterior
div_page2

# %%
#fazendo uma limpeza das aparições
aparicoes = [i.text for i in div_page2]
aparicoes