cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}ERRO: Por favor, digite um númeor inteiro válido.{cores["limpar"]}')
            continue
        except (KeyboardInterrupt):
            print(f'{cores["vermelho"]}Usuário preferiu não digitar esse número{cores["limpar"]}')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cores["amarelo"]}{c}{cores["limpar"]} - {cores["azul"]}{item}{cores["limpar"]}')
        c += 1
    print(linha())
    opc = leiaInt(f'{cores["verde"]}Sua opção: {cores["limpar"]}')
    return opc