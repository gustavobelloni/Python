while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if valor < 0:
        break
    for c in range(1, 11):
        resul = valor * c
        print(f'{valor} x {c} = {resul}')
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
