# DICIONÁRIO AJUDA NA HORA DE ORGANIZAR E LOCALIZAR AS INFORMAÇÕES DAS LISTAS
informacoes_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60}
# KEYS = LOCALIZA A CHAVE DA LISTA (NOME, IDADE, ALTURA)
print(informacoes_pessoa.keys())
# VALUES = LOCALIZA OS VALORES DA LISTA (CAROL, 18, 1.60)
print(informacoes_pessoa.values())
# ITEMS = LOCALIZA O PAR DE CHAVES DA LISTA ('nome', 'Carol'), ('idade', 18), ('altura', 1.6)
print(informacoes_pessoa.items())

for item in informacoes_pessoa.items():
    print(item)
    # O ITEM ESTA LOCALIZANDO AS INFORMAÇÕES E NAO OS VALORES

    print(item[1])

    # O NUMERO 1 LOCALIZA O ITEM DENTRO DA LISTA(LEMBRE COMEÇA DO 0, SENDO NOME O 0 E CAROL O 1 )
