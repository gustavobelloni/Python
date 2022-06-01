import contatos_uteis

try:
    # contatos = contatos_uteis.csv_para_contatos('dados/contatos.csv', encoding='UTF-8')
    # contatos_uteis.contatos_para_pickle(contatos, 'dados/contatos.pickle')

    # contatos = contatos_uteis.pickle_para_contatos('dados/contatos.pickle')
    # contatos_uteis.contatos_para_json(contatos, 'dados/contatos.json')

    contatos = contatos_uteis.json_para_contatos( 'dados/contatos.json')


    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('Arquino não encontrado.')
except PermissionError:
    print('Sem permissão de escrita.')
