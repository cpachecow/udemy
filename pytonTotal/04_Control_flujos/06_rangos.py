# La funcion 'range()', se genera un listado de numeros enteros el cuál tiene tres parámetros:
#  1.- Si solo se incluye el primer número, el rango será hasta donde será el rango, iniciando de cero hasta el número sin incluir.
#  2.- Si se agrega otro número, se indicará desde dónde hasta dónde se ejecutará el rango.
#  3.- Si se incluye, indica cada cuántos números se saltará.

num = range(50)
print(num)
print('\n')

num = range(20, 50)
print(num)
print('\n')

lista = list(range(20)) # Se puede crear una lista muy rápida con la función range
print(lista)
print('\n')

for i in range(10):
    print(i)
print('\n')

for i in range(5,10):
    print(i)
print('\n')

for i in range(0,50, 5):
    print(i)
print('\n')

# Sumar los cuadrados de un rango del 1 al 15 inclusive.
suma_cuadrados = 0
for i in range(1,16):
    cuad = i**2
    suma_cuadrados += cuad
print(suma_cuadrados)

