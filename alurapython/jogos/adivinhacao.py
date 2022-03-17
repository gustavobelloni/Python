print('-' * 33)
print('Bem vindo ao jogo de adivinhação!')
print('-' * 33)

numero_secreto = 42

chute = int(input('Digite o seu número: '))

print(f'Você digitou {chute}')

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print('Você acertou!')
else:
    if maior:
        print('Você errou, o seu chute foi maior do que valor correto!')
    elif menor:
        print('Você errou, seu chute foi menor do que valor correto!')

print('Fim do jogo!')
