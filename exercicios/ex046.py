cores = {'vermelho': '\033[31m',
         'verde': ' \033[32m',
         'amarelo': '\033[33m'}
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(f'{cores["vermelho"]}BUM! {cores["verde"]}BUM! {cores["amarelo"]}POOOW!')
