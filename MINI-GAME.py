from turtle import Turtle
import turtle

# # INICIALIZAR UMA TURTLE
# t = Turtle()

# # DEFINIR VELOCIDADE ENTRE 1 E 10, SENDO 1 O MAIS LENTO
# t.speed(1)

# # MOVIMENTAR A TURTLE PARA FRENTE
# t.forward(100)

# # ROTACIONAR EM X GRAUS PARA DIREITA
# t.right(90)
# t.forward(100)

# # ROTACIONAR EM X GRAUS PARA DIREITA
# t.left(90)
# t.forward(100)

# # ROTACIONAR APARA TRÁS
# t.backward(200)

# input()


# DESAFIO
t = Turtle()
t.speed(1)
while True:

    direcao = input('Qual direção devemos ir, para frente ou para trás? ')
    if direcao == 'frente':
        distancia = int(input('Quantos pixels deseja percorrer? '))
        rotacionar = input(
            'Rotacionar para direita, esquerda ou não rotacionar? ')
        if rotacionar == 'direita':
            graus = int(input('Quantos graus deseja rotacionar? '))
            t.right(graus)
        elif rotacionar == 'esquerda':
            graus = int(input('Quantos graus deseja rotacionar? '))
            t.left(graus)
        t.forward(distancia)

    if direcao == 'trás':
        distancia = int(input('Quantos pixels deseja percorrer? '))
        rotacionar = input(
            'Rotacionar para direita, esquerda ou não rotacionar? ')
        if rotacionar == 'direita':
            graus = int(input('Quantos graus deseja rotacionar? '))
            t.right(graus)
        elif rotacionar == 'esquerda':
            graus = int(input('Quantos graus deseja rotacionar? '))
            t.left(graus)
        t.backward(distancia)

    resposta = input('Deseja continuar andando? ')
    if resposta not in ('sim', 's'):
        break
