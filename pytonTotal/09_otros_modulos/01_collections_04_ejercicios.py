# Práctica Módulo Collections 1

# Aplica un Counter (contador) sobre la lista de números entregada a continuación, 
# y almacénalo en una variable llamada contador

from collections import Counter, defaultdict, deque

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)



# Práctica Módulo Collections 2

# Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave 
# buscada, se cargue con el string "Valor no hallado".

# Carga el diccionario, al menos, con el siguiente par de datos:
# palabra clave = edad
# valor = 44
# Utiliza el método defaultdict del módulo Collections.

mi_diccionario = {}
mi_diccionario = defaultdict(lambda: 'Valor no hallado')
mi_diccionario['edad'] = 44

print(mi_diccionario)



# Práctica Módulo Collections 3

# Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite insertar y eliminar elementos por ambos extremos.
# Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir del módulo collections. Los elementos iniciales de la 
# lista se brindan a continuación. ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
# La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)
lista_ciudades.append('Santiago')
print(lista_ciudades)
lista_ciudades.appendleft('Buenos Aires')
print(lista_ciudades)