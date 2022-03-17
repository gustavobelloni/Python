cores = {'limpar': '\033[m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}
print(f'{cores["amarelo"]}-={cores["limpar"]}' * 20)
print(f'{cores["verde"]}Analisador de Triângulos{cores["limpar"]}')
print(f'{cores["amarelo"]}-={cores["limpar"]}' * 20)
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print(f'Os segmentos acima {cores["verde"]}PODEM{cores["limpar"]} formar um triângulo!')
else:
    print(f'Os segmentos acima {cores["vermelho"]}NÃO PODEM{cores["limpar"]} formar um triângulo!')
