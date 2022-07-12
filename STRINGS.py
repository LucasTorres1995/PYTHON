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
# FAZ A CONTAGEM DA POSIÇÃO DESTA LETRA, LEMBRANDO QUE SEMPRE COMEÇA DO ZERO
print(nome_curso.find('ção'))
# SUBSTITUI UMA INFORMAÇÃO PELA OUTRA
print(nome_curso.replace('Video', 'Musica'))
# EXEMPLO DE MODIFICAÇÃO DE SITE
print('https://sc.olx.com.br/?o=98q=relogio'.replace('relogio', 'carro'))


# DESAFIO
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')

# COMO EXTRAIR PARTES DE UMA STRING (SLICE)

cartao = '5555 9999 8888 77774'
print(cartao[0:5])  # NESTE CASO ELE BUSCA AS INFORMAÇÕES CONTIDAS DE 0 ATE 4
# NESTE CASO ELE BUSCA A INFORMAÇÃO CONTIDA NO LUGAR DE POSIÇÃO NUMERO 7, LEMBRANDO QUE SEMPRE COMEÇA DO '0'
print(cartao[7])
# NESTE CASO ELE VAI CONTAR DE TRAS PARA FRENTE A INFORMAÇÃO CONTIDA NO NUMERO INFORMADO
print(cartao[-5])
print(cartao[0:])  # NESTE CASO ELE IMPRIME TUDO ATE O FINAL
print(cartao[-5:])  # NESTE CASO INICIA EM UMA POSIÇÃO E VAI ATE O FINAL
print(cartao[:-5])  # NESTE CASO ELE INICIA DO 0 ATE O FINAL INFORMADO
# NESTE CASO ELE INDICA A POSIÇÃO DE DETERMINADO STRING
print(cartao.index('8'))

# NESTE CASO ELE BUSCARÁ UMA PARTE DAS INFORMAÇÕES
# OBS QUE A ULTIMA INFORMAÇÃO DA STRING NAO FOI APRESENTADA (4), PARA QUE ISSO OCORRA, DEVERA COLOCAR O "+1 NO FINAL"
indice_a = cartao.rindex('9')
indice_b = cartao.rindex('4')
print(cartao[indice_a:indice_b])
print(cartao[indice_a:indice_b+1])

# FUNÇÃO SPLIT É USADA PARA SEPARAR STRINGS (ELE NAO INCLUI O SEPARADOR)
print(cartao.split(' '))  # NESTE CASO ELE SEPAROU TUDO QUE CONTINHA ESPAÇO
print(cartao.split('8'))  # SEPAROU E EXCLUIU O SEPARADOR

# COMO CONCATENAR (JUNTAR/COMBINAR) STRINGS
cartao_espaco = cartao.split(' ')
# NESTE CASO TODAS AS INFORMAÇÕES ONDE CONTINHAM ESPAÇO, FORAM SUBSTITUIDO POR #
print('#'.join(cartao_espaco))
# NESTE CASO TODAS AS INFORMAÇÕES ONDE CONTINHAM ESPAÇO, FORAM SUBSTITUIDO POR X
print('X'.join(cartao_espaco))
# NESTE CASO TODAS AS INFORMAÇÕES ONDE CONTINHAM ESPAÇO, FORAM SUBSTITUIDO POR 2 ESPAÇOS
print('  '.join(cartao_espaco))
