n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {m:.1f}')
if m >= 7:
    print('O aluno está APROVADO!')
elif 5 <= m < 7:
    print('O aluno está em RECUPERAÇÃO')
elif m < 5:
    print('O aluno está REPROVADO!')
