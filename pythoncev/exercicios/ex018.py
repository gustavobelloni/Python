import math
ang = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tangente:.2f}')
