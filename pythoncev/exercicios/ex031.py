cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'ciano': '\033[36m',
         'amarelo': '\033[33m'}
distancia = int(input('Qual é a distância da sua viagem em Km? '))
print(f'{cores["azul"]}Você está prestes a fazer uma viagem de {cores["amarelo"]}{distancia}Km{cores["limpar"]}')
if distancia <= 200:
    p1 = distancia * 0.50
    print(f'{cores["ciano"]}O valor da sua passagem é de R${p1:.2f}{cores["limpar"]}')
else:
    p2 = distancia * 0.45
    print(f'{cores["ciano"]}O valor da sua passagem é de R${p2:.2f}{cores["limpar"]}')
