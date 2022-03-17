import datetime
cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} {cores["verde"]}é BISSEXTO{cores["limpar"]}')
else:
    print(f'O ano de {ano} {cores["vermelho"]}NÃO é BISSEXTO{cores["limpar"]}')
