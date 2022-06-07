from cpf_cnpj import DocCnpj, DocCpf
from telefonesbr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

''' CPF
- Validação -> Deve conter 11 dígitos e utilizar biblioteca de validação
- Máscara -> 999.999.999-99'''

cpf = input('Digite seu CPF: ')
cpf_objeto = DocCpf(cpf)
print(cpf_objeto)

''' CNPJ
- Validação -> Deve conter 14 dígitos e utilizar biblioteca de validação
- Máscara -> 99.999.999/9999-99'''

cnpj = input('Digite seu CNPJ:')  # 40726353000198
cnpj_objeto = DocCnpj(cnpj)
print(cnpj_objeto)

''' Telefone/Celular
- Validação -> Deve conter de 10 a 11 caracteres(inclui código de área)
- Máscara -> (99)9999-9999'''

telefone = input('Digite seu número de telefone: ')
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

''' Data e Hora
- Deve salvar o momento de um cadastro
- Deve retornar data e hora no formato pt-br
- Deve ser capaz de mostrar há quanto tempo um usuário está cadastrado'''

hoje = DatasBr()
print(f'Hoje é dia {hoje}')

''' CEP
- Validação -> Deve conter 8 dígitos 
- Máscara -> 99999-999
- Acessar WebService ViaCEP e retornar Endereço
'''

cep = input('Digite seu CEP:')  # 01001000
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(f'{bairro}, {cidade}, {uf}')
