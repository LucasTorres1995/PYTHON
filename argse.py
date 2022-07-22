# AGRS POSICIONAIS
# PERMITE VOCE COLOCAR DIVERSOS VALORES DENTRO DE UMA VARIAVEL, BASTA COLOCAR O *
# ANTES DA VARIAVEL QUE DESEJA COLOCAR OS VALORES, COMO NO EXEMPLO
# def somar(*valores, b):
#     for valor in valores:
#         b+= valor
#     print(b)
# somar(10, 20, 5, b= 5)

# KWARGS
# QUANDO QUEREMOS RECEBER INFORMAÇÕES INFINITAS DENTRO DE UMA VARIAVEL, USAMOS DOIS * (**). É IMPORTANTE NOMEAR
def concatenar(**nomes):
    frase = ''
    for nome in nomes.values():
        frase += nome + ' '
    print(frase)


concatenar(a='Lucas', b='Guimaraes', c='Barbosa')
