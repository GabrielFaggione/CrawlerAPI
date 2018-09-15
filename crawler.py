from urllib.request import Request, urlopen


def search(url,string):
    print ('url procurado: '+ url)
    print ('string procurada: '+ string)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8').lower()
    quant = webpage.count(string.lower())
    return quant
