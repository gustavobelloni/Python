from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'O atleta tem {idade} anos!')
if idade <= 9:
    print('O atleta participa da categoria MIRIM')
elif idade <= 14:
    print('O atleta participa da categoria INFANTIL')
elif idade <= 19:
    print('O atleta participa da categoria JUNIOR')
elif idade <= 25:
    print('O atleta participa da categoria SÊNIOR')
else:
    print('O atleta participa da categoria MASTER')
