# Módulo Collections nos ayuda a completar y a manipular las estructuras de datos 
# (listas, tuplas, diccionarios, etc) de una manera eficiente.

from collections import namedtuple

# ------------
# namedtuple: Provee una forma simple de crear estructura de datos.
# ------------

# Declarando nametuple()
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

# Añadiendo valores
ariel = Persona('Ariel', 1.80, 85)

# Accediendo al valor 'nombre' por índice
print(ariel[0])

# Accediendo al valor altura 
print(ariel.altura)

# Accediendo al valor peso 
print(ariel.peso)

