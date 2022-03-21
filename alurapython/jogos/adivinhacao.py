from random import randint


def jogar():
    print('-' * 33)
    print('Bem vindo ao jogo de adivinhação!')
    print('-' * 33)

    numero_secreto = randint(1, 100)
    tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil  (2) Médio (3) Difícil')

    nivel = int(input('Defina um nível: '))
    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

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
            print(f'Você acertou e fez {pontos} pontos!')
            break
        else:
            if maior:
                print('Você errou, o seu chute foi maior do que valor correto!')
            elif menor:
                print('Você errou, seu chute foi menor do que valor correto!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f'O número era {numero_secreto}')
    print('Fim do jogo!')


if __name__ == '__main__':
    jogar()
