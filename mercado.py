import requests
from bs4 import BeautifulSoup
import pandas as pd

prods = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

produto_nome = input('qual produto vc deseja?\n')

url = 'https://lista.mercadolivre.com.br/'


try:
    resposta = requests.get(url + produto_nome, headers=headers)
    resposta.raise_for_status() #mostra se tem erro na requisição 

    site = BeautifulSoup(resposta.text, 'html.parser')

    produtos = site.find_all('li', attrs={'class': 'ui-search-layout__item'})
    if not produtos:
        print("produto nao encontrado")
        exit()

    print(f" Processando {len(produtos)} produtos...")

    for produto in produtos:
    
        #titulo
        titulo = produto.find('h3', attrs={'class': 'poly-component__title-wrapper'})

        #link
        link = produto.find('a', attrs={'class': 'poly-component__title'})

        #valor
        valorProduto = produto.find('div', attrs={'class': 'poly-price__current'})
        valor_real = valorProduto.find('span', attrs={'class': 'andes-money-amount__fraction'})
        valor_centavos = valorProduto.find('span', attrs={'class': 'andes-money-amount__cents--superscript-24'})
        
        titulo_texto = titulo.text.strip() if titulo else "Título não encontrado"
        #link
        link_url = link['href'] if link else "Link não encontrado"
        if valor_real:
            valor_final = f"R$ {valor_real.text.strip()}"
            if valor_centavos:
                valor_final += f",{valor_centavos.text.strip()}"
        else:
            valor_final = "Preço não encontrado"
        prods.append([titulo_texto, link_url, valor_final])

    #colocando em uma planilha
    if prods:
        prod = pd.DataFrame(prods, columns=['Titulo', 'Link', 'Valor'])
        nome_arquivo = f"produtos_{produto_nome}.xlsx"
        prod.to_excel(nome_arquivo, index=False)
        
        '''
        #print
        print("Titulo do produto: ", titulo.text, link['href'], valor_real.text)
        print("Link: ", link['href'])
        if(valor_centavos):
            print("Preco produto: R$", valor_real.text + ', ' + valor_centavos.text)
        else:
            print("Preco produto: R$", valor_real.text)
        print('\n\n')
        '''
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")