n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opção = ''
while opção != 5:
    soma = n1 + n2
    multiplicação = n1 * n2
    print("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'A soma de {n1} + {n2} é {soma}')
    elif opção == 2:
        print(f'A multiplicação de {n1} x {n2} é {multiplicação:.2f}')
    elif opção == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}')
    elif opção == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando')
        exit()
    else:
        print('Opção inválida! Escolha uma das opções abaixo.')
