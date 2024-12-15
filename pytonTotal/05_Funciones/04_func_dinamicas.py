# Funciones que nos permitiran validar varios cáculos.

# Validar que tres números de una lista están en un rango de 100 a 1.000
def valid_rango(lista):
    for i in lista:
        if i in range(100,1001):
            return True # Si dentro de la lista hay un valor intermedio que cumple, se retorna el valor y corta el ciclo.
        else:
            pass # acá no agrego return False, dado que si no cumple algun número, sale del ciclo inmediatamente.

    return False # Por esto se agrega al final, solo queda como False, si ningun numero de la lista cumple.

resul1= valid_rango([77,200,2000])
print(resul1)

# Validar y mostrar los números que cumplen el rango (100 a 1000) de una lista
def valid_rango2(lista):
    lista_encontrada = []
    for i in lista:
        if i in range(100,1001):
            lista_encontrada.append(i)
        else:
            pass
    return lista_encontrada

result2 = valid_rango2([99,999,1002])
print(result2)

# Crea una función (todos_positivos) que reciba una lista de números como parámetro,
#   y devuelva True si todos los valores de una lista son positivos, y False si al menos
#   uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

def todos_positivos(lista):
    lista_numeros = []
    for i in lista:
        if i < 0:
            return False
        else:
            pass
    return True

lista_numeros = [22,23,200]
resul3 = todos_positivos(lista_numeros)
print(resul3)

# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros)
#   siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

def suma_menores(lista):
    suma = 0
    for i in lista:
        if i in range(0,1000):
            suma += i
        else:
            pass
    return suma

lista_numeros = [-1,5,25,1,1000]
resul4 = suma_menores(lista_numeros)
print(resul4)

# Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una
#  lista (lista_numeros), y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista):
    cuenta = 0
    for i in lista:
        if((i > 0) and (i%2==0)):
            cuenta += 1
        else:
            pass
    return cuenta

lista_numeros = [-1,2,3,4,5,6,7,8,9,11,12,13,41,28]
resul5 = cantidad_pares(lista_numeros)
print(resul5)
