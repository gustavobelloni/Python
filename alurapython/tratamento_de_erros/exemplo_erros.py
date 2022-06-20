'''
if True:  # IndentationError -> Erro de identação
    print('Olá, mundo')  # SyntaxError se colocar um ')' a mais
'''

''' 
frase = 'Olá mundo'
print(frase.ola)  # AttributeError -> não existe o atributo 'ola'
'''


def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError('dividir() deve receber apenas argumentos inteiros')
        
    try:
        aux = dividendo / divisor
    except:
        print(f'Não foi possível dividir {dividendo} por {divisor}')
        raise

    return aux


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f'O resultado da divisão de 10 por {divisor} é {resultado}')
    

'''try:
    testa_divisao(2.5)  # ZeroDivisionError -> erro por dividir por 0 (zero)
except ZeroDivisionError as E:
    print('Erro de divisao por zero')
 # except Exception as E:
 #     print('Tratamento generico')


print('Programa encerrado')'''

try:
    print('O fluxo está aqui')
    raise ValueError
except Exception:
    print('Agora ele veio para cá')
print('E enfim, ele continua...')