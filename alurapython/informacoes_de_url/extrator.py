import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:  # __eq__
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'{self.url}\nParâmetros: {self.get_url_parametros()}' \
               f'\nURL Base: {self.get_url_base()}'

    def __eq__(self, other):
        return self.url == other.url


url = 'bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real'
extrator_url = ExtratorURL(url)
valor_dolar = 5.50
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
quantidade = int(extrator_url.get_valor_parametro('quantidade'))


if moeda_destino == 'dolar' and moeda_origem == 'real':
    valor_conversao = quantidade * valor_dolar
    print(f'O valor de {quantidade} dólares é igual a {valor_conversao:.2f} reais')
elif moeda_destino == 'real' and moeda_origem == 'dolar':
    valor_conversao = quantidade / valor_dolar
    print(f'O valor de {quantidade} reais é igual a {valor_conversao:.2f} dólares')
else:
    print(f'Câmbio de {moeda_origem} para {moeda_destino} não está disponível')
