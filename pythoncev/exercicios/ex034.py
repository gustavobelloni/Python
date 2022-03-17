cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'ciano': '\033[36m'}
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print(f'Quem ganhava R${cores["ciano"]}{salario:.2f}{cores["limpar"]} passa a ganhar R${cores["verde"]}{aumento:.2f}'
      f'{cores["limpar"]} agora.')
