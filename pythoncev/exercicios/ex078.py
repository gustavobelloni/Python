valores = []
maior = 0
menor = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
    if pos == 0:
        maior = menor = valores[pos]
    else:
        if valores[pos] > maior:
            maior = valores[pos]
        if valores[pos] < menor:
            menor = valores[pos]
print('=-' * 30)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
