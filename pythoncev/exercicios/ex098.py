from time import sleep


def contagem(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print('-=' * 20)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    sleep(2.5)
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += pas
        print('FIM!')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= pas
        print('FIM!')


# Programa Principal
contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contagem(i, f, p)
