# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
#     La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
#     Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
#     Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada
#     (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje
#     según la suma de estos valores:

#    Si la suma es menor o igual a 6: "La suma de tus dados es {suma_dados}. Lamentable"
#    Si la suma es mayor a 6 y menor a 10: "La suma de tus dados es {suma_dados}. Tienes buenas chances"
#    Si la suma es mayor o igual a 10: "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
# ** Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
from random import randint

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return (dado1, dado2)

def evaluar_jugada(da1, da2):
    d1, d2 = da1, da2
    suma_dados = d1 + d2
    if(suma_dados <= 6):
        return f'La suma de tus dados es {suma_dados}. Lamentable'
    elif(suma_dados > 6 and suma_dados < 10):
        return f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    elif(suma_dados >= 10):
        return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora !!!'

dado1, dado2 = lanzar_dados()
# print(f'Dado[1] = {dado1} :: Dado[2] = {dado2}')
evaluar_jugada(dado1, dado2)

# Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros),
# y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos)
# y eliminando el valor más alto. El orden de los elementos puede modificarse.
#
# Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].
#
# Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función,
# y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

def reducir_lista(lista):
    lista = set(lista) #eliminamos los repetidos
    lista = list(lista)
    lista.pop() #eliminamos el último valor más alto
    return lista

def promedio(lista):
    suma = 0
    for i in lista:
            suma += i
    promedio = suma/len(lista)
    return(promedio)

lista_numeros = [1,1,2,2,3,3,4,4,5,10,5,6,7,7,7,8,9,9]

result2 = reducir_lista(lista_numeros)
#print(result2)
prom = promedio(result2)
#print(prom)


# Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar).
#    Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
#
# Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado
# del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista
# con valores y llamarla lista_numeros).
#
#  Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla
#  (devolverla como lista vacía []).
#
#   Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
from random import randint

def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    aleatorio = randint(0,1)
    return moneda[aleatorio]

def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        lista.clear()
        return f'La lista se autodestruirá, valor lista {lista}'
    elif moneda == 'Cruz':
        return f'La lista fue salvada, valor lista {lista}'


lista02 = [1,2,3,'Pepe',200,300]
res_moneda = lanzar_moneda()
print(res_moneda)
p = probar_suerte(res_moneda, lista02)
print(p)




