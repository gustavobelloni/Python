preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista em dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    desc10 = preço - (preço * 10 / 100)
    print(f'A sua compra de R${preço:.2f}, com desconto de 10%, vai custar R${desc10:.2f} no final')
elif opção == 2:
    desc5 = preço - (preço * 5 / 100)
    print(f'A sua compra de R${preço:.2f}, com desconto de 5%, vai custar R${desc5:.2f} no final')
elif opção == 3:
    x2 = preço / 2
    print(f'''A sua compra será parcelada em 2x de R${x2:.2f} SEM JUROS
Sua compra de R${preço:.2f} vai custar R${preço:.2f} no final.''')
elif opção == 4:
    juros20 = preço + (preço * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print(f'''Sua compra está parcelada em {parcelas}x de R${juros20 / parcelas:.2f} COM JUROS
sua compra de R${preço:.2f} vai custar R${juros20:.2f} no final.''')
else:
    print('Opção inválida!')
