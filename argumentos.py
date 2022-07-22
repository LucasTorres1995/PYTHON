# ARGUMENTOS POSICIONAIS E ARGUMENTOS NOMEADOS
# ARGUMENTOS POSICIONAIS VAO RESPEITAR A ORDEM COLOCADA DENTRO DA FUNÇÃO
# ARGUMENTOS NOMEADOS VÃO RESPEITAR A ORDEM DA FUNÇÃO ORIGINAL

# EXEMPLO ARGUMENTO POSICIONAIS
# def exibir_preco(nome_produto, preco):
#     print(f'{nome_produto} está no valor de: {preco}')


# exibir_preco('Iphone', 5000)

# # EXEMPLO DE ARGUMENTO NOAMEADOS


# def exibir_preco(nome_produto, preco):
#     print(f'{nome_produto} está no valor de: {preco}')


# exibir_preco(preco=5000, nome_produto='Iphone')

# # EXISTE TAMBÉM A MANEIRA DE OBRIGAR A NOMEAR A FUNÇÃO QUE ESTA ATRIBUINDO VALOR, EXEMPLO:
# # O * EXIGE QUE COLOQUE O NOME DA FUNÇÃO A QUAL ESTA ATRIBUINDO VALOR, ASSIM EVITA ERROS0


# def exibir_preco(*, nome_produto, preco):
#     print(f'{nome_produto} está no valor de: {preco}')


# exibir_preco(preco=5000, nome_produto='Iphone')

# DESAFIO
def gerar_objeto_personalizado(cor, *, altura, formato):
    print(
        f'Este objeto possui as seguintes caracteristicas: {cor}, {altura}, {formato}')


gerar_objeto_personalizado('vermelho', altura=1.00, formato='redondo')
