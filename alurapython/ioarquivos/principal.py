arquivo_contatos = open('dados/contatos.csv', encoding='UTF-8')

for linha in arquivo_contatos:
    print(linha, end='')
    