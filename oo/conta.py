# self é a referencia que está sendo criada no console

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto... {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


Conta()
