# INDENTAÇÃO SE TRATA DOS ESPAÇOS NECESSÁRIOS PARA O CÓDIGO RODAR CORRETAMENTE
# SEMPRE QUE HOUVER CATEGORIA "FILHA" DEVERÁ TER UMA INDENTAÇÃO E SE HOUVER UMA FILHA DA FILHA, DEVERA TER 2 INDENTAÇÕES

import time


def PensarPor10Segundos():
    print('pensando')
    time.sleep(10)
    print('Lembrei!')


if 10 > 5:
    print('10 é maior que 5')


class BemVindo():
    def __init__(self):
        print('Bem vindo')


oi = BemVindo()
