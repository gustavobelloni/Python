times = ('Corinthians', 'Palmerias', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Time em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
