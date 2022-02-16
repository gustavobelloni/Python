num = float(input('Qual é o preço do produto? R$ '))
desc = num - (num * 5 / 100)
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}'.format(num, desc))
