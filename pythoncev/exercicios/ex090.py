resul = dict()
resul['nome'] = str(input('Nome: '))
resul['media'] = float(input(f'Média de {resul["nome"]}: '))
print(f'Nome é igual a {resul["nome"]}')
print(f'Média é igual a {resul["media"]}')
if resul['media'] < 6:
    print('Situação é igual a REPROVADO')
else:
    print('Situação é igual a APROVADO')

