from random import shuffle
# El juego consiste en elegir un palito y si es el mas corto, pierdes.
# De una lista de palos, se debe ordenar en forma aleatoria, para luego solicitar al usuario
# un palo. Si seleeciona el menor pierde, en caso contrario sigue jugando.

# Lista inicial
palitos = ['-','--','---','----']

# Mezclar palitos
def mezclar_palitos(lista):
    shuffle(lista)
    return(lista)

# Solicitar intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input('Elige in número del 1 al 4: ')

    return(int(intento))

# Comprobar intento
def comp_intento(lista, intento):
    if lista[intento-1] == '-':
        print('Perdiste!, a lavar los platos... jajajaja!')
    else:
        print('Te salvaste!')

    print(f'Te ha tocado el palito: {lista[intento-1]}')

palitos_mezclados = mezclar_palitos(palitos)
intento = probar_suerte()

comp_intento(palitos_mezclados, intento)
