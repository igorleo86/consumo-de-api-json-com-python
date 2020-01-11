import requests #requests - requisição de bibliotecas online / dados da URL
import json #buscar funções do json
import pandas #exportar dados em excel
import decimal

url = "http://data.fixer.io/api/latest?access_key=65526a5ba0df11253889f4ab7c61f3ad"
print("Acessando base de dados do Fixer.io...")
resposta = requests.get(url)
print(resposta)
if resposta.status_code == 200: #status_code - código de acesso à página URL
    print("Acesso realizado com sucesso!")
    print("Buscando informações...")
    dados = resposta.json()
    dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'], 2) #round - arredondar número. Especificar número de casas decimais (, 2)
    euro_real = round(dados['rates']['BRL']/dados ['rates']['EUR'], 2)
    bitcoin_real = round(dados['rates']['BRL']/dados['rates']['BTC'], 2)

    print('1 dollar vale ',dolar_real, 'reais') #mostrar valor do dolar
    print('1 euro vale ',euro_real, 'reais') #mostrar valor do euro
    print('1 bitcoin vale ',bitcoin_real, 'reais') #mostrar valor do bitcoin
    print('Exportando resultado em tabela Excel')
    tela = pandas.DataFrame({'Moedas': ['Dolar', 'Euro', 'Bitcoin'], #pandas.DataFrame - informações da tabela Excel
                            'Valores': [dolar_real, euro_real, bitcoin_real]})
    tela.to_csv('valores.csv', index=False, sep=";", decimal=",")
    print('Arquivo exportado com sucesso!')
else:
    print("Erro na base de dados")
