from random import randint
print('=-' * 20)
print('Vamos jogar PAR ou ÍMPAR')
print('=-' * 20)
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper()[0].strip()
    print('-' * 20)
    computador = randint(0, 10)
    soma = valor + computador
    resul = soma
    if resul % 2 == 0:
        resul = 'P'
    else:
        resul = 'I'
    final = resul
    if final == 'P':
        final = 'PAR'
    else:
        final = 'ÍMPAR'
    print(f'Você jogou {valor} e o computador {computador}. Total de {soma} deu {final}')
    if resul == escolha:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
        cont += 1
    else:
        break
print(f'GAME OVER! Você vencer {cont} vezes')
