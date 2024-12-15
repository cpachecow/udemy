# Sets: Son inmutables, por lo tanto no pueden agregar ítems y no se guardan con una
#       ubicación específica. Adicionlamente hay dos formas de iniciarlos y no acepta valores repetidos,
#       si estos son agregados, los elimina. No acepta lista y diccionarios, si tuplas.

# Estructura básica
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,'hola'}
print(type(otro_set))
print(otro_set)

otro_set = {4,4,4,4,5,5,5,6,6,6}
print(otro_set)

# Largo de un set
mi_set = set([1,2,3,4,5,6])
print(len(mi_set))

# Indicar si un valor está en el set
print(9 in mi_set) # Devuelve 'True' si encuentra el valor, en caso contrario 'False'

# Union de dos sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print("Tipo: union de sets =>",type(s3))
print("Union de sets:", s3)

# Agregar un valor a un Set
s1.add(4)
print(s1)

# Eliminar un valor a un Set
s1.remove(1) # Si no está el valor a eliminar, arrojará error.
print(s1)

# Eliminar un valor a un Set aleatoreo
s1.pop()
print(s1)

# Dejar vacío un set
s1.clear()
print(s1)






