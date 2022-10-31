from codigo.bytebank import Funcionario
import pytest


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given(contexto)
        entrada = '13/03/2000'
        esperado = 22

        funcionario_teste = Funcionario('teste', entrada, 1111)

        # When(ação)
        resultado = funcionario_teste.idade()

        # Then(desfecho)
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        # Given(contexto)
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)

        # When(ação)
        resultado = lucas.sobrenome()

        # Then(desfecho)
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given(contexto)
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        # When(ação)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        # Then(desfecho)
        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given(contexto)
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

        # When(ação)
        resultado = funcionario_teste.calcular_bonus()

        # Then(desfecho)
        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # Given(contexto)
            entrada = 1000000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

            # When(ação)
            resultado = funcionario_teste.calcular_bonus()

            # Then(desfecho)
            assert resultado

