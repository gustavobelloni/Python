print('-' * 23)
print('  CADASTRE UMA PESSOA')
print('-' * 23)
total = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()[0].strip()
    if idade >= 18:
        total += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    print('-' * 20)
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')

