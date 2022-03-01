''' num = [2, 4, 7, 8]
num[2] = 15
num.append(7)
num.sort()
num.insert(3, 5)
num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos.') '''

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c,v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
