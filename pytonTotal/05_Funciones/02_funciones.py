# Funciones:
#  Son partes de código reutilizable que se puede llamar cuantas veces uno necesite.
#  Podemos pasar variables por parámetro tambien. Y se inician con def nombre_funcion():

def hola_mundo():
    print("Hola Mundo!")

hola_mundo()

def hola_nombre(nombre):
    '''
    Saluda y retorna un texto con un nombre por parámetro
    :param nombre:
    :return:
    '''
    print(f"Hola {nombre}")
hola_nombre('Andrea')

def cuadrado(numero):
    print(f'El cuadrado de {numero} es {numero**2}')

cuadrado(3)

