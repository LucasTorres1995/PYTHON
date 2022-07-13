# CONDICIONAIS
# maior_de_idade = True
# possui_carteira_de_trabalho = True
# filho_do_dono = False
# esta_trabalhando_atualmente = True
# possui_veiculo_proprio = False

# PODE TRABALHAR AQUI SE FOR MAIS DE IDADE E POSSUIR CARTEIRA DE TRABALHO OU SE FOR FILHO DO DONO
#print((maior_de_idade == True and possui_carteira_de_trabalho == True) or (filho_do_dono == True))

# CONTRATAMOS PESSOAS COM CARTEIRA DE TRABALHO QUE NAO TENHA VEICULO PROPRIO
# print((possui_carteira_de_trabalho == True and possui_veiculo_proprio == False)) #ou
# print((possui_carteira_de_trabalho == True and not possui_veiculo_proprio))

# COMPARAR RESULTADOS DE DUAS VARIAVEIS, OU SEJA, ESTA VERIFICANDO SEM AMBAS TEM O MESMO VALOR DE TRUE OU FALSE E DIZENDO SE SAO IGUAIS
#print(maior_de_idade and esta_trabalhando_atualmente)

# # DESAFIO
# from asyncio.proactor_events import _ProactorBaseWritePipeTransport


# possui_passaporte = False
# passagem_comprada = False
# menor_de_idade = False

# # 1 SÓ PODE VIAJAR SE POSSUIR PASSAPORTE E TIVER PASSAGEM COMPRADA E NAO FOR MENOR DE IDADE
# print((possui_passaporte and passagem_comprada and not menor_de_idade))


# # 2 SÓ PODE VIAJAR SE POSSUIR PASSAPORTE OU TIVER A PASSAGEM COMPRADA E NAO FOR MENOR DE IDADE
# print((possui_passaporte or passagem_comprada) and not menor_de_idade)


# # 3 SÓ PODE VIAJAR SE NAO POSSUIR PASSAPORTE OU TIVER A PASSAGEM COMPRADA E NAO FOR MENOR DE IDADE
# print((not possui_passaporte or passagem_comprada) and not menor_de_idade)


# # 4 NAO PODE VIAJAR SE NAO POSSUIR PASSAPORTE OU NAO TIVER A PASSAGEM COMPRADA E FOR MENOR DE IDADE
# print((not possui_passaporte or passagem_comprada) and not menor_de_idade)


# # PODE VIAJAR SE POSSUIR PASSAPORTE E TIVER A PASSAGEM COMPRADA E NAO FOR MENOR DE IDADE
# print((possui_passaporte and passagem_comprada == True and not menor_de_idade))

#-----------------------------------------------------------------------------------------------------#
# OPERADORES DE IGUALDADE
# == OU is
# ambos tem a mesma função mas pode apresentar resultados diferentes dependendo do local onde rodará python


#-----------------------------------------------------------------------------------------------------#
# CONVERSÃO DE TIPOS
# MAIS COMUNS

# int(NUMEROS INTEIROS)   str(TEXTO)   float(NUMEROS DECIMAIS)   list()   tuple()     dict()

# EXEMPLOS

# NESTE CASO ELE CONVERTE O STRING PARA NUMERO INTEIRO
idade = input('Qual é sua idade?')
print(int(idade) > 18)

# NESTE EXEMPLO É CONSIDERADO A ALTURA QUE É NUMERO DECIMAL
altura = input('Qual sua altura?')
print(float(altura) > 1.80)
