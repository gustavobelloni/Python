num = ''
cont = 0
soma = 0
while num != 0:
    num = int(input('Digite um número [0 para parar]: '))
    soma += num
    if num != 0:
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
