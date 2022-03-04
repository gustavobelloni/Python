''' def título(txt):
    print('-' * 20)
    print(txt)
    print('-' * 20)


título(f'{"Gutão":^20}') '''


''' def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(4, 5)
soma(7, 2)
soma(3, 9) '''


'''def contador(* núm):
    tam = len(núm)
    print(f' Recebi os valores {núm} e possui {tam} números')


contador(5, 6, 8, 7 )
contador(8, 9)
contador(5, 0)'''


'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 4, 9, 1, 0, 2]
dobra(valores)
print(valores)'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(9, 2, 4)
