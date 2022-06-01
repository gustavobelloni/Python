import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encoding='UTF-8'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)
        
        for linha in leitor:
            id, nome, email = linha
        
            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos

def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo: # 'wb' - abrir o arquivo em modo binário no modo escrita
        pickle.dump(contatos, arquivo)


def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo: # 'rb' - abrir o arquivo em modo binário no modo leitura
        contatos = pickle.load(arquivo)
    
    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json)


def _contato_para_json(contato):
    return contato.__dict__


def json_para_contatos(caminho):
    contatos = []

    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            c = Contato(**contato) # -> id=contato['id'], nome=contato['nome'], email=contato['email'] -> vai desenpacotar os contatos
            contatos.append(c)

    return contatos