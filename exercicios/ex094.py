galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0].strip()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
        if continuar  in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
média = soma / len(galera)
print('-=' * 20)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {média:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')
