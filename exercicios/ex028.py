from random import randint
from time import sleep
cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'magenta': '\033[35m',
         'vermelho': '\033[31m'}
computador = randint(0, 5)
print(f'{cores["amarelo"]}-=-{cores["limpar"]}' * 20)
print(f'{cores["verde"]}Vou pensar em um número entre 0 e 5. Tente adivinhar...{cores["limpar"]}')
print(f'{cores["amarelo"]}-=-{cores["limpar"]}' * 20)
jogador = int(input('Em que número eu pensei? '))
print(f'{cores["magenta"]}PROCESSANDO...{cores["limpar"]}')
sleep(2)
if jogador == computador:
    print(f'{cores["verde"]}PARABÉNS! Você conseguiu me vencer! Tá de hack?{cores["limpar"]}')
else:
    print(f'{cores["vermelho"]}ERRRRRRRRRROU, Eu pensei no número {computador} e não no {jogador}{cores["limpar"]}')
