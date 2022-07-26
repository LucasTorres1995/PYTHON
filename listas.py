# FUNÇÃO SORT FAZ A ORGANIZAÇÃO DAS LISTAS
# valores = [30, 20, 5, 27, 35, 90, 87]
# valores.sort()
# print(valores)

# # REVERSE=TRUE FAZ COM QUE A LISTA FIQUE EM ORDEM DECRESCENTE
# valores.sort(reverse=True)
# print(valores)

# REVERSE FAZ COM QUE A LISTA SEJA REPRODUZIDA DE TRÁS PARA FRENTE
# valores.reverse()
# print(valores)

# ZIP LONGEST, CRIA LISTAS E SE FALTAR ALGUMA INFORMAÇÃO NA LISTA ELE COMPLETA COM NONE
# from itertools import zip_longest

# produto = ['Iphone 5S', 'Iphone 12', 'Iphone 14', 'Galaxy S23']
# valores = ['1000', '4000', '8000']

# for produto, valores in zip_longest(produto, valores):
#     print(f'O celular {produto} está custando: {valores}')

# A FUNÇÃO ZIP NÃO MOSTRARÁ O PRODUTO QUE ESTIVER SEM PREÇO, AO CONTRARIO DO ZIP_LONGEST QUE APENAS MARCA A INFORMAÇÃO COMO NONE ATÉ QUE SEJA ADICIONADA A INFORMAÇÃO
# for produto, valores in zip(produto, valores):
#     print(f'O celular {produto} está custando: {valores}')
