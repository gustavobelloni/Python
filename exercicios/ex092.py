from datetime import datetime
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: '))
    ano = int(input('Ano de nascimento: '))
    pessoa['idade'] = datetime.now().year - ano
    pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if pessoa['ctps'] == 0:
        break
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = int(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 40) - datetime.now().year)
    break
print('-=' * 20)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')
