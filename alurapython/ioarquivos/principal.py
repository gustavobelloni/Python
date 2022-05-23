'''try:
    with open('dados/contatos.csv', encoding='UTF-8') as arquivo_contatos:
        for linha in arquivo_contatos:
                print(linha, end='')
except FileNotFoundError:
    print('Arquino não encontrado.')
except PermissionError:
    print('Sem permissão de escrita.')'''