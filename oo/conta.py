# self é a referencia que está sendo criada no console

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} reais de {self.__titular} ')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)


conta = Conta(123, 'Gustavo', 55.5, 1000.0)
conta2 = Conta(321, 'Nico', 70.0, 1000.0)
