from datetime import datetime


# data_nascimento = datetime.strptime(input('Quando é  sua data de nascimento'), '%d/%m/%Y') # preenchimento de data
# print(type(data_nascimento))

# data_atual = datetime.now() # busca a data atual
# print(data_atual)

dia_atual = datetime(2020, 5, 7)
aniversario = dia_atual - datetime.now()
print(aniversario)
