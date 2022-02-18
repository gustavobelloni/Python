nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Analisando seu nome...')
print(f'''Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}
Seu nome tem ao todo {len(nome)-nome.count(' ')} letras
Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras''')
