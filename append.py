# APPEND SERVE PARA ADICIONAR UMA INFORMAÇÃO DENTRO DA LISTA, ESSA INFORMAÇÃO SERA ADICIONADA COMO ULTIMO ITEN DA LISTA
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anos = [2020, 2021, 2022]

valores.append(11)
print(valores)

# EXTEND SERVE PARA UNIR LISTAS
valores.extend(anos)
print(valores)

# GERAR NOVA LISTA
nova_lista = valores + anos
print(nova_lista)

# INDEX BUSCA O VALOR DENTRO DA LISTA
valor = valores.index(5)
print(valor)

# INSERIR VALOR DENTRO DA LISTA
# O NUMERO 3 INDICA A ONDE IRÁ ENTRAR A INFORMAÇÃO PASSADA
anos.insert(3, 2031)
print(anos)

# EXTRAIR
ano_2022 = anos.pop(2)
print(ano_2022)

# REMOVER O VALOR DA LISTA
anos.remove(2021)
# del anos[1]    # DEL É UMA OPCAO PARA REMOVER
print(anos)

# DEL SERVE TAMBEM PARA REMOVER UMA LISTA DENTRO DOS VALORES
del valores[1:5]
print(valores)

# COUNT TAMBEM SERVE PARA CONTAR AS OCORRENCIAS QUE SE REPETEM DENTRO DE UMA LISTA
print(valores.count(6))

# RESETAR VALORES DA LISTA
valores.clear()
print(valores)
