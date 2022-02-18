a = 3
b = 5
print(f'Os valores são \033[31m{a}\033[m e \033[34m{b}\033[m')
nome = 'Guanabara'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;29m'}
print(f'{cores["azul"]}{nome}{cores["limpa"]}')
