def tabuada(num):
    for multiplicador in range(0, 11):
        print(f'{num} x {multiplicador} = {num * multiplicador}')
    return num


print('-=' * 20)
print(f'{"Tabuada":^40}')
tabuada(6)
print('-=' * 20)
