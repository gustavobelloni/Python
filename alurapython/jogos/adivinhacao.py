print('-' * 33)
print('Bem vindo ao jogo de adivinhação!')
print('-' * 33)

numero_secreto = 42
chute = int(input('Digite o seu número: '))

print(f'Você digitou {chute}', end=', ')

if chute == numero_secreto:
    print('Você acertou!')
else:
    print('Você errou!')
    print(f'O número era {numero_secreto}')
print('Fim do jogo!')