cores = {'vermelho': '\033[31m',
         'limpar': '\033[m'}


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'{cores["vermelho"]}Erro! Digite um número inteiro válido{cores["limpar"]}')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')