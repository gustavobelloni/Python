from utilidadesCeV import moeda

valor = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10%, temos  {moeda.moeda(moeda.aumentar(valor, 10))}')
