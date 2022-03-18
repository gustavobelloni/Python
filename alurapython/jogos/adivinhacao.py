from random import randint

print('-' * 33)
print('Bem vindo ao jogo de adivinhação!')
print('-' * 33)

numero_secreto = randint(1, 100)
tentativas = 3 


for rodada in range(1, tentativas+1):
    print(f'Tentativa {rodada} de {tentativas}')
    chute = int(input('Digite um número entre 1 e 100: '))
    print(f'Você digitou {chute}')
    if chute < 1 or chute > 100:
        print('Você deve digitar um número entra 1 e 100!')
        continue

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

print(f'O número era {numero_secreto}')
print('Fim do jogo!')
