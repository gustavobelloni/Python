from telefonesbr import TelefonesBr
import re

telefone = '552132789311'
telefone_objeto = TelefonesBr(telefone)
# padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
# resposta = re.search(padrao, telefone)
# print(resposta.group())
print(telefone_objeto)

''' CPF
- Validação -> Deve conter 11 dígitos e utilizar biblioteca de validação
- Máscara -> 999.999.999-99 '''

''' CNPJ
- Validação -> Deve conter 14 dígitos e utilizar biblioteca de validação
- Máscara -> 99.999.999/9999-99'''

''' Telefone/Celular
- Validação -> Deve conter de 10 a 11 caracteres(inclui código de áre)
- Máscara -> (99)9999-9999'''

''' Data e Hora
- Deve salvar o momento de um cadastro
- Deve retornar data e hora no formato pt-br
- Deve ser capaz de mostrar há quanto tempo um usuário está cadastrado'''

''' CEP
- Validação -> Deve conter 8 dígitos 
- Máscara -> 99999-999
- Acessar WebService ViaCEP e retornar Endereço
'''
