def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Chao')

    return otra_funcion

@decorar_saludo
def mayusc(texto):
    print(texto.upper())


def minusc(texto):
    print(texto.lower())

mayusc("Los Prisioneros")

minusc("La Maquina de hacer pájaros")