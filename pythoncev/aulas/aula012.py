nome = str(input('Qual é o seu nome? ')).title().strip()
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Nai':
    print('Que nome feminino bonito!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')
