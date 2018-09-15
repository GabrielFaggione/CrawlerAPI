# -*- coding: utf-8 -*-
import requests
import json

"""
Testes unitários realizados utilizando pytest
valores da palavra chave utilizada foram recolhidos no dia 15/09
"""

def testApi():
    r = requests.get('http://127.0.0.1:5000/') 
    assert r.status_code == 200 # teste para verificar a resposta da servidor

def testGetAndPutApi():
    urlList = 'https://www.python.org/;https://www.pygame.org/news;http://docs.python-requests.org/en/master/' # Lista das urls procuradas
    lookFor = 'python' # palavra procurada
    data_put = {'url':urlList, 'string':lookFor} # dict para usar como parametro do put
    data_get = {'url':'https://www.python.org/'} # dict para usar como parametro do get

    r_put = requests.put('http://127.0.0.1:5000/api/', params = data_put) # obj request do put
    r_get = requests.get('http://127.0.0.1:5000/api/', params = data_get) # obj request do get

    resultado_put = json.loads(r_put.text) # instanciando uma dict atraves do json para poder analisar os dados
    resultado_get = json.loads(r_get.text) # idem

    #testes para verificar as saídas dos casos de put solicitados
    assert len(resultado_put) == len(urlList.split(';')) # teste para ver se a quantidade de buscas é igual a quantidade de urls
    assert resultado_put['https://www.python.org/'] == {'python':202}
    assert resultado_put['https://www.pygame.org/news'] == {'python':22}
    assert resultado_put['http://docs.python-requests.org/en/master/'] == {'python':34}
    #teste para verificar se o get condiz com o put respectivo
    assert resultado_get['https://www.python.org/'] == resultado_put['https://www.python.org/']
