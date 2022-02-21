from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
ano = nasc + 18
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}')
elif idade == 18:
    print('Você tem q se alistar IMEDIATAMENTE!')
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano}.')

