continuar = 'S'
cont = soma = maior = menor = 0
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / cont
print(f'Você digitou {cont} números e a média foi {média}')
print(f'O maior valor foi de {maior} e o menor foi de {menor}')


