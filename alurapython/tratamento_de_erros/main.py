from exceptions import SaldoInsuficienteError,OperacaoFinanceiraError
from leitor import LeitorDeArquivo


class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_conta_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.cliente= cliente
        self.__set_agencia(agencia)
        self.__numero = numero
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidas = 0
        ContaCorrente.total_conta_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_conta_criadas
        
    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo agencia deve ser um inteiro', value)

        if value <= 0:
            raise ValueError('O atributo agencia deve ser maior que zero')

        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo número deve ser um inteiro')

        if value <= 0:
            raise ValueError('O atributo número deve ser maior que zero')
                      
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo saldo deve ser um inteiro zero')

        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError('O valor a ser sacado não pode ser menor que zero') 
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidas += 1
            E.args = ()
            raise OperacaoFinanceiraError('Operação não finalizada!') from E
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError('O valor a ser sacado não pode ser menor que zero')
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError('', self.saldo,  valor)
        self.saldo -= valor
    
    def depositar(self, valor):
        self.saldo += valor

def main():
    import sys

    contas = []
    while True:
        try:
            nome = input('Nome do cliente:\n')
            agencia = input('Numero de agencia:\n')
            breakpoint()
            numero = input('Numero da conta corrente:\n')
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)}(s) contas criadas')
            sys.exit()



 # if __name__ == '__main__':
 #     main()

 # conta_corrente1 = ContaCorrente(None, 400 , 123546)
 # conta_corrente2 = ContaCorrente(None, 401 , 123446)
 # try:
 #     conta_corrente1.sacar
 #     print('ContaCorrente1 Saldo: ', conta_corrente1.saldo)
 #    print('ContaCorrente2 Saldo: ', conta_corrente2.saldo)
 # except OperacaoFinanceiraError as E:
 #     breakpoint()
 #     pass

with LeitorDeArquivo('arquivo.txt') as leitor:
    leitor.ler_proxima_linha()
    