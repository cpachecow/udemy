# Módulo Collections nos ayuda a completar y a manipular las estructuras de datos 
# (listas, tuplas, diccionarios, etc) de una manera eficiente.

# Elemento Counter: Nos permitirá contar el contenido desde una estuctura de datos, 
#                   devolviendo un diccionario.

from collections import Counter

# Lista
numeros = [1,1,1,1,1,2,2,2,3,3,3,3,3,3,4,4]
print(Counter(numeros)) # -> Counter({3: 6, 1: 5, 2: 3, 4: 2})

# Tupla
palabras = ('pa','pe','pa','pi','pi','pi','pi','pi','pi','po','po','po','pu','pi','pe','pe','po')
print(Counter(palabras))

# String I
oracion = 'tres tristes trigres trigo trigaban en un trigal'
print(Counter(oracion.split()))

# String II
oracion = 'tinguiririca'
print(Counter(oracion))


# ------------
# most_common: Indicará el(los) dato(s) que más se repiten de una estructura de datos, retorna una tupla.
# ------------

serie = Counter([1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3])

# most_common: Si no envío ningún argumento, retornará una tupla indicando el valor de cada elemento y 
#              cuántas veces se repite cada uno.
print(f'Más comunes: {serie.most_common()}') # > Más comunes: [(1, 11), (2, 5), (3, 4)]

# most_common: Si paso como argumento el '1', retornará una tupla indicando el valor que más se repite.
print(f'El más común: {serie.most_common(1)}') # Más común: [(1, 11)]

# most_common: Si paso como argumento el '2', retornará una tupla indicando los dos valores que más se repiten.
print(f'Los dos más comunes: {serie.most_common(2)}') # > Los dos más comunes: [(1, 11), (2, 5)]

# most_common: Si paso como argumento el '3', retornará una tupla indicando los tres valores que más se repiten.
palabra = Counter('pppppppiiiiiiooooooooooooooooooooooooooouuuuuuuuuuuuuuuubvbbbbb')
print(f'Las tres más comunes: {palabra.most_common(3)}') # > Las tres más comunes: [('o', 27), ('u', 16), ('p', 7)]

# Pasar a una lista los elementos de una estructura de datos con Counter, devolviento sus elementos únicos.
numeros = [1,1,1,1,1,1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4]
lista = list(serie)
print(lista)
