nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conheçer!')
print(f'Seu primeiro nome é {nome.title().split()[0]}')
print(f'Seu último nome é {nome.title().split()[len(nome.split())-1]}')
