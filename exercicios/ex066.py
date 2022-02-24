soma = cont = 0
while True:
    num = int(input('Digite um valor (0 para parar): '))
    if num == 0:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores  foi {soma}!')
