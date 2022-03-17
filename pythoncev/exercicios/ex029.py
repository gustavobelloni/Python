cores = {'limpar': '\033[m',
         'vermelho': '\033[31m',
         'ciano': '\033[36m'}
velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade-80) * 7
if velocidade > 80:
    print(f"""{cores['vermelho']}MULTADO! Você excedeu o limite permitido que é de 80Km/h
    Você deve pagar uma multa de R${multa}!{cores['limpar']}""")
print(f'{cores["ciano"]}Tenha um bom dia! Dirija com segurança!{cores["limpar"]}')