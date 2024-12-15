def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Chao')

    return otra_funcion

def mayusc(texto):
    print(texto.upper())


def minusc(texto):
    print(texto.lower())

mayusc_decorada = decorar_saludo(mayusc)

mayusc_decorada('Soda Stereo')

minusc("Los Prisioneros")