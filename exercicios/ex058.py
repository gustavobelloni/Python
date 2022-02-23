from random import randint
computador = randint(0, 10)
print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")
tentativas = 0
num = ''
while num != computador:
    num = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if num < computador:
        print('Mais... Tente novamente.')
    elif num > computador:
        print('Menos... Tente novamente.')
print(f'Acertou com {tentativas} tentativas. Parabéns!')
