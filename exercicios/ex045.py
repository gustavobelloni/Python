from time import sleep
from random import randint
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 10)
print(f'Computador jogou {lista[computador]}')
print(f'Jogador jogou {lista[jogador]}')
print('-=' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador GANHOU!')
    elif jogador == 2:
        print('Computador GANHOU!')
elif computador == 1:
    if jogador == 0:
        print('Computador GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador GANHOU!')
elif computador == 2:
    if jogador == 0:
        print('Jogador GANHOU!')
    elif jogador == 1:
        print('Computador GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
