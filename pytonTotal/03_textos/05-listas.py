# ** Listas **
#       Objetos que están entre corchetes y son separados con comas,
#       pueden ser se cualquier tipo y son mutables.

mi_lista = ['a','b','c']
print(type(mi_lista))

# Para saber la cantidad de ítems de una lista, se usa el len
print(len(mi_lista))

# Se puede obtener parte de la lista, indexandolas
print(mi_lista[0])

# Se pueden concatenar
mi_lista2 = ['d','e','f']
print(f"Lista1 y Lista2 concatenadas: {mi_lista + mi_lista2}") #se puede guardar en otra variable tambien

# Son mutables, o sea se pueden cambiar los elementos de una lista
mi_lista3 = mi_lista + mi_lista2
print(f"Lista3: {mi_lista3}")
mi_lista3[0] = "Lelo"
print(f"Lista3 modificada: {mi_lista3}")

# Uso append, para agregar elementos a las listas.
mi_lista3.append("wolfx")
print(f"Lista3 con un texto agregado al final: {mi_lista3}")

# Uso pop, para eliminar un elemento de una lista que paso por parámetro,
# si no lo agrego, Python entiende que eliminará el último útem de la lista.
mi_lista4 = mi_lista2
print(f"Lista4 original: {mi_lista4}")
mi_lista4.pop()
print(f"Lista4 modificada: {mi_lista4}")

# Para ordenar la lista Ascendente, se utiliza sort
lista5 = [2,5,7,9,10]
lista5.sort()
print(lista5)

# Para ordenar la lista Descendente, se utiliza reverse
lista5.reverse()
print(lista5)
# Tanto sort() como reverse() generan la acción de ordenar, pero no entregan un valor.

# lista20 = ['uno','Hola un ejecutivo','dos','Hola un ejecutivo','tres','Hola un ejecutivo','veinte','seis', 'cuatro']
# print('Hola un ejecutivo' in lista20)
# print(lista20.count('Hola un ejecutivo'))
# print(len(lista20))


# s = 'Hola un ejecutivo'
# matched_indexes = []
# i = 0
# length = len(lista20)

# while i < length:
#     if s == lista20[i]:
#         matched_indexes.append(i)
#     i += 1

# print(lista20[matched_indexes[-1]-1:len(lista20)])


