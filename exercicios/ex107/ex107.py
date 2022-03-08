from utilidadesCeV import moeda

valor = float(input('Digite o preço: R$ '))
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'aumentando 10%, temos R${moeda.aumentar(valor, 10)}')
