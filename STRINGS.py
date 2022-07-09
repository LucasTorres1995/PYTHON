# STRINGS DINÂMICOS
# DESAFIO 1
nomee = 'Fernando'
hobby = 'ouvir música'
print(f'Olá sou o {nomee} e gosto de{hobby}')

# DESAFIO 2
b = 'ba'
parte2 = 'nica'
a = 'a'
r = 'ri'
parte1 = 'eletrô'
t = 'te'

print(f'{b}{t}{r}{a} {parte1}{parte2}')


# METODOS COMUNS DE STRINGS
nome_curso = "Edição de Video"
print(nome_curso.upper())  # COLOCA EM MAIUSCULO
print(nome_curso.lower())  # COLOCA EM MINISCULO
print(nome_curso.strip())  # REMOVE ESPAÇO EM BRANCO
print(nome_curso.lstrip())  # REMOVE ESPAÇO EM BRANCO DA ESQUERDA
print(nome_curso.rstrip())  # REMOVE ESPAÇO EM BRANCO DA DIREITA
print(nome_curso.find('ção'))  # FAZ A CONTAGEM DA POSIÇÃO DESTA LETRA, LEMBRANDO QUE SEMPRE COMEÇA DO ZERO
print(nome_curso.replace('Video', 'Musica')) # SUBSTITUI UMA INFORMAÇÃO PELA OUTRA
print('https://sc.olx.com.br/?o=98q=relogio'.replace('relogio', 'carro')) # EXEMPLO DE MODIFICAÇÃO DE SITE


#DESAFIO 
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
