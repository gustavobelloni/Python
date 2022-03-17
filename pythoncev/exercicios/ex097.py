def mensagem(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
mensagem(f'{"Gustavo Guanabara"}')
mensagem(f'{"Curso de Python no Youtube"}')
mensagem(f'{"CeV"}')
