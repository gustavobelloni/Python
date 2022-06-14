idades = [39, 30, 27, 18]  # -> Lista []
print(idades, '-> Lista []')

idades.append(15)  # append -> adiciona no final o valor 15
print(idades, '-> Adicionado o valor 15')

idades.remove(30)  # remove -> remove o valor 30, se tiver mais de um valor 30, remove o primeiro
print(idades, '-> Remove o valor 30')

# idades.clear()  # clear -> remove todos os elementos
# print(idades, ' -> Limpa a lista por completo')

print(28 in idades, '-> Valor 28 não está na lista')  # Verifica se possui o valor 28

print(18 in idades, '-> Valor 18 está na lista')  # Verifica se possui o valor 18

if 15 in idades:
    idades.remove(15)  # Se 15 estiver dentro de idades, será removido
print(idades, '-> Valor 15 foi removido em um "if"')

idades.insert(0, 20)  # Insire o valor em um local específico
print(idades, '-> Valor 20 inserido na posição 0 atraver de um "insert"')

idades.extend([41, 50])  # Coloca mais de um valor na lista
print(idades, 'Coloca o valor 41 e 50 com o "extend"')

# array:
print('Através da criação de uma array e usando o for, mostrará as idades no ano que vem:')
idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)
print(idades_no_ano_que_vem)

# outra maneira de ser feita:
idades_no_ano_que_vem = [(idade+1) for idade in idades]
print(idades_no_ano_que_vem)
print('Filtrar idades maiores que 21:')
print('Idades maiores que 21:', [idade for idade in idades if idade > 21])

# uma lista é mutável -> problemas com isso:


def faz_processamento_de_visualizacao(lista):
    print(len(lista))
    lista.append(13)


faz_processamento_de_visualizacao(idades)
print(idades)
# devido a mutabilidade, não é possivel saber o que será feito com a lista


def faz_processamento_de_visualizacao(lista=None):
    if lista is None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


print(faz_processamento_de_visualizacao())
print(faz_processamento_de_visualizacao())
print(faz_processamento_de_visualizacao())
print(faz_processamento_de_visualizacao())