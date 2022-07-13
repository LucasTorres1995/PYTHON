import random
from datetime import datetime

nome_completo = input('Digite seu nome completo:')

idade = int(input('Digite sua idade:'))

data_nascimento = datetime.strptime(
    input('Quando é  sua data de nascimento:'), '%d/%m/%Y')


data_atual = datetime.now()

cartoes = ['50,00', '250,00', '120,00']
cartao = random.choice(cartoes)

print(f'Olá {nome_completo}, seu registro foi concluído com sucesso no dia, {data_atual.day}/{data_atual.month}/{data_atual.year}. \n Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de R$ {cartao}')
