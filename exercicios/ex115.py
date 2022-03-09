cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde': '\033[32m'}

while True:
    print('-' * 30)
    print(f'{"Menu pricipal":^30}')
    print('-' * 30)
    print(f'{cores["amarelo"]}1{cores["limpar"]} - {cores["azul"]}Ver pessoas cadastradas{cores["limpar"]}')
    print(f'{cores["amarelo"]}2{cores["limpar"]} - {cores["azul"]}Casatrar nova Pessoa{cores["limpar"]}')
    print(f'{cores["amarelo"]}3{cores["limpar"]} - {cores["azul"]}Sair do Sistema{cores["limpar"]}')
    print('-' * 30)
    opção = int(input('Sua opção: '))
    if opção == 1:
        print('-' * 30)
        print(f'{"Opção 1":^30}')
        print('-' * 30)
    elif opção == 2:
        print('-' * 30)
        print(f'{"Opção 2":^30}')
        print('-' * 30)
    elif opção == 3:
        break

