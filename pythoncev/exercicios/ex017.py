import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hi = sqrt(pow(co, 2) + pow(ca, 2))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')

