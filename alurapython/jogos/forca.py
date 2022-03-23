def jogar():
    print('-' * 27)
    print('Bem vindo ao jogo de forca!')
    print('-' * 27)

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = str(input('Qual letra? ')).lower().strip()

        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1

        print(letras_acertadas)

    print('Fim do Jogo!')


if __name__ == '__main__':
    jogar()
