''' def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(c=3,  a=2) '''


'''def teste():
    x = 8
    print(f'Na função teste, n vale{n}')
    print(f'Na função teste, x vale {x}')


n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale  ')'''


'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 global vale {n1}')'''


'''def somar (a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 4)
r3 = somar(3)
print(f'Os resultados doram {r1}, {r2} e {r3}')'''


'''def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''


'''def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')'''
