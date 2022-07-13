# GERA VALORES ALEATÓRIOS

import random

print(random.random())  # GERA UM VALOR ALEATORIO ENTRE 0.0 A 1.0
# GERA UM VALOR DECIMAL ENTRE OS VALORES MINIMO E MAXIMO INFORMADOS
print(random.uniform(4, 20))
# GERA UM VALOR INTEIRO ENTRE O MINIMO E MAXIMO INFORMADOS
print(random.randint(4, 20))

cores = ['verde', 'azul', 'amarelo']
print(random.choices(cores))  # GERA UMA COR ALEATORIA

print(random.shuffle(cores))
print(cores)  # GERA UMA COR ALEATORIA

# DESAFIO
moeda = ['cara', 'coroa']
print(random.choices(moeda))  # GERA UMA COR ALEATORIA

print(random.randint(10, 100))
