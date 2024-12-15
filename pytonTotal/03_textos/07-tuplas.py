# Tuplas: Son muy similares a las listas, pero son inmutables
#         Esto implica que una vez que son asignadas, no pueden ser variadas.
#         Ocupan menos espacio de memoria y son más rápidas.

# Estructura básica
t = (1,2,3,1)
print(type(t))

# Asignacion multiple: Tiene que haber el mismo número de variable como de valores de la tupla
x,y,z,k = t
print(x,y,z,k)

# Largo de una tupla
print(len(t))

# Contar cuántas veces está un valor dado
print(t.count(1))

# Verificar la ubicación de un valor en una tupla
print(t.index(2))

# Convertir una tupla en lista
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(type(mi_lista))