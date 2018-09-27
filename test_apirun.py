# -*- coding: utf-8 -*-
import requests
import json
from crawler import search

"""
Testes unitários realizados utilizando pytest
valores da palavra chave utilizada foram recolhidos no dia 15/09
"""

def testApi():
    r = requests.get('http://127.0.0.1:5000/') 
    assert r.status_code == 200, "Servidor não esta respondendo corretamente"  # teste para verificar a resposta da servidor

def testPutApi():
    urlList = 'https://www.globo.com/;https://www.folha.uol.com.br/' # Lista das urls procuradas
    lookFor = 'São Paulo' # palavra procurada
    data_put = {'url':urlList, 'string':lookFor} # dict para usar como parametro do put

    r_put = requests.put('http://127.0.0.1:5000/api/', params = data_put) # obj request do put
    # teste para verificar a resposta do servidor ao executar o put
    assert r_put.status_code == 200

    resultado_put = json.loads(r_put.text) # instanciando uma dict atraves do json para poder analisar os dados
    # teste para ver se a quantidade de buscas é igual a quantidade de urls
    assert len(resultado_put) == len(urlList.split(';'))

    #testes para verificar se o valor recebido no put condiz com a saida do resultado
    assert lookFor in resultado_put['https://www.globo.com/']
    assert lookFor in resultado_put['https://www.folha.uol.com.br/']


def testGetApi():
    data_get = {'url':'https://www.globo.com/'} # dict para usar como parametro do get
    lookFor = 'São Paulo' # palavra procurada no test de Put da api

    r_get = requests.get('http://127.0.0.1:5000/api/', params = data_get) # obj request do get
    # teste para verificar a resposta do servidor ao exercutar o get
    assert r_get.status_code == 200

    resultado_get = json.loads(r_get.text) # instanciando uma dict atraves do json para poder analisar os dados
    # teste para verificar se o valor recebido do get condiz com o put solicitado a cima
    assert lookFor in resultado_get['https://www.globo.com/']