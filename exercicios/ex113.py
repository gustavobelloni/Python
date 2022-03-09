cores = {'limpar': '\033[m',
         'vermelho': '\033[31m'}
while True:
    try:
        inteiro = int(input('Digite um número Inteiro: '))
    except:
        print(f'{cores["vermelho"]}ERRO: Por favor, digite um número inteiro válido.{cores["limpar"]}')
    else:
        break
while True:
    try:
        real = float(input('Digite um número Real: '))
    except:
        print(f'{cores["vermelho"]}ERRO: Por favor, digite um número real válido{cores["limpar"]}')
    else:
        break
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
