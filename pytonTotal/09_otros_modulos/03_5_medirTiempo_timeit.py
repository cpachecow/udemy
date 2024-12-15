import timeit

# El módulo timeit, sirve para registrar tiempos más acotados y precisos. 
# Por lo tanto se puede medir la eficiencia de dos funciones, por ejemplo, 
# con mayor exactitud. Para que funcione timeit, requiere tres parámetros
# 
# 1.- Declaración o statement: que sera un texto con el uso de una función
# 2.- Setup: Es la función o bloque de programa que se guarda en una variable texto,
# 3.- Number: Indica cuántas veces se repitirá el código, para ver cuánto tiempo demora.

# def prueba_for(numero):
#     lista = []
#     for num in range(1, numero + 1):
#         lista.append(num)
#     return lista

# def prueba_while(numero):
#     lista = []
#     contador = 1
#     while contador <= numero :
#         lista.append(contador)
#         contador+=1
#     return lista

# Prueba timeit() 1: 

declaracion = '''
prueba_for(10)
'''
mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion,mi_setup,number=10000000)
print(f'Duración prueba_for: {duracion}')


# Prueba timeit() 2: 

declaracion2 = '''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero :
        lista.append(contador)
        contador+=1
    return lista
'''

duracion2 = timeit.timeit(declaracion2,mi_setup2,number=10000000)
print(f'Duración prueba_while: {duracion2}')
print((1-(duracion/duracion2))*100)