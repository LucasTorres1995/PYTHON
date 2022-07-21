# CONTINUE E BREAK
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rock':
        continue
    print(f'{estilo}')


estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(f'{estilo}')
