# CONDICIONAIS IF ELIF ELSE
# if é condicional
# elif é um condicional que só passa para a opção de baixo caso essa nao seja a condição
# else caso não esteja nas condições

# MEU TESTE
# trabalho_terminado = input('Você acabou o trabalho?')
# if (str(trabalho_terminado == True)):
#     print('Sextou!!!')
# else:
#     print('Termine o trabalho')


# numero_atrasos = int(input('Quantos atrasos você tem?'))
# if numero_atrasos >= 3:
#     print('Vá para diretoria')
# elif numero_atrasos == 2:
#     print('Essa é sua segunda falta')
# elif numero_atrasos == 1:
#     print('Essa é sua primeira falta')
# else:
#     print('Pode entrar')


# velocidade = int(input('Qual a velocidade do veículo?'))
# if velocidade <= 50:
#     print('Não foi multado')
# elif velocidade >= 51 and velocidade <= 60:
#     print('Levou multa de 2 pontos')
# elif velocidade >= 61 and velocidade <= 75:
#     print('Levou multa de 3 pontos')
# else:
#     print('Levou multa de 7 pontos')

# CHAINING REDUZ A QUANTIDADE DE CODIGO, PODE COMPARAR COM O CODIGO A CIMA O MESMO EXEMPLO. AS LINHAS 28 E 30 E O EXEMPLO POSTERIOR NAS LINHAS 39 E 41
# velocidade = int(input('Qual a velocidade do veículo?'))
# if velocidade <= 50:
#     print('Não foi multado')
# elif  51 <= velocidade <= 60:
#     print('Levou multa de 2 pontos')
# elif  61 <= velocidade <= 75:
#     print('Levou multa de 3 pontos')
# else:
#     print('Levou multa de 7 pontos')

# DESAFIO CABELO
# tamanho_cabelo = int(input('Quantos centimetros tem seu cabelo? '))
# if tamanho_cabelo <= 20:
#     print('Custa R$50,00')
# elif 21 <= tamanho_cabelo <= 30:
#     print('Custa R$70,00')
# elif 31 <= tamanho_cabelo <= 50:
#     print('Custa R$100,00')
# else:
#     print('Favor consultar na recepção')


# OPERADOR TERNÁRIO
# DESTA MANEIRA SE ECONOMIZA LINHAS E TEMPO
# passaporte = True
# print('Favor embarcar') if passaporte else print(
#     'Favor, emita seu passaporte')


# DESAFIO TERNÁRIO
# velocidade = 101
# print('Siga em frente') if velocidade <= 100 else print(
#     'Você foi multado')
