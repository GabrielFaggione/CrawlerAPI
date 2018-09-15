from flask import Flask, request
from flask_restplus import Resource, Api
from urllib.request import Request, urlopen

app = Flask(__name__) # instancia um objeto FLask
api = Api(app, version='1.0', title='Crawler API', # instancia a API
    description='A simple crawler')

urls = {} # dict responsável por guardar a url e as pesquisas relacionadas as mesmas

def search(url,string):
    # Funcao responsavel pela varredura das urls
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #Método utilizado para poder ler sites que possuem segurança contra "varreduras"
    web_byte = urlopen(req).read() # Lemos a url atual
    webpage = web_byte.decode('utf-8').lower() #codificamos a url lida para utf-8 e transformamos toda a string para lowercase
    quant = webpage.count(string.lower()) # verificamos a ocorrencia da string dentro do site
    return quant # retornamos o valor obtido

@api.route('/api/')
class UrlCommand(Resource):
    @api.doc(params={'url': 'Adicionar a url a ser pesquisada, como por exemplo: \n .../api/?url=https://www.python.org/'})
    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def get(self):
        url = request.args.get('url') # recebe o parametro passado
        return {url: urls[url]} # retorna a dict correspondente ao valor do parametro passado

    @api.doc(responses={
        200: 'Success',
        400: 'Validation Error'})
    @api.doc(params={'url': 'Adicionar as urls separadas por ";", como por exemplo: \n .../api/?url=https://www.python.org/;https://pypi.org/'})
    @api.doc(params={'string':'Adicionar a string a ser procurada após o ultimo url, como por exemplo: \n ...pipy.org/&string=Python'})
    def put(self):
        url_string = request.args.get('url') # recebe os urls a serem verificados
        string = request.args.get('string') # recebe a string a ser verificada
        resultado = {} # dict para mostrar o resultado final das varreduras
        for url in url_string.split(";"): # quebra a string(url_string) em uma lista e a roda item por item
            if url not in urls:
                urls[url] = {string: search(url, string)}
            else:
                urls[url].update({string: search(url, string)})
            """
            No if case a cima é analisado se a url já possui alguma pesquisa realizada, caso não haja é adicionado na dict urls a nova url
            e caso a url já pertença a dict é apenas atualizado com o novo valor pesquisado 
            """
            resultado[url] = {string: search(url, string)} # somado a ultima pesquisa realizada para a exibição no final
        return resultado # retorna a pesquisa atual realizada, com os valores dos sites passados

if __name__ == '__main__':
    app.run(debug=True)