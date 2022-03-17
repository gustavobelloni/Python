valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor / (anos * 12)
print(f'Para pagar uma casa de R${valor:.2f} em {anos} a prestação será de R${prestacao:.2f}')
if prestacao > salario * 30 / 100:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo CONCEDIDO!')
