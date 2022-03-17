from random import randint

print('-' * 33)
print('Bem vindo ao jogo de adivinhação!')
print('-' * 33)

numero_secreto = randint(0, 100)
tentativas = 3
while tentativas > 0:
    print(f'Você tem {tentativas} tentativas')
    chute = int(input('Digite um número de 0 a 100: '))
    print(f'Você digitou {chute}')
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if acertou:
        print('Você acertou!')
        break
    else:
        if maior:
            print('Você errou, o seu chute foi maior do que valor correto!')
        elif menor:
            print('Você errou, seu chute foi menor do que valor correto!')
    tentativas -= 1
print(f'O número era {numero_secreto}')
print('Fim do jogo!')
