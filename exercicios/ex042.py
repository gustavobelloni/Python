reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
escaleno = reta1 != reta2 != reta3 != reta1
equilátero = reta1 == reta2 == reta3
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print(f'Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if equilátero:
        print('EQUILÁTERO!')
    elif escaleno:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
