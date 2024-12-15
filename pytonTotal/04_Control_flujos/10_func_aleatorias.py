from random import randint
from random import uniform
from random import random
from random import choice
from random import shuffle


# randint(x,y) arroja un número entero aleatorio en un rango.
num = randint(1,60)
print(num)

# uniform(x,y) arroja un número float en un rango.
num2 = uniform(1,10)
num2 = round(num2,3)
print(num2)

# random(): no necesita parámetros y arroja un número float entre 0 y 1.
num3 = random()
num3 = round(num3,3)
print(num3)

# choice(): Selecciona un objeto de una cadena, lista, tupla etc y lo muestra de forma aleatoria.
colores = ['Verde', 'Amarillo', 'Rojo']
rand_color = choice(colores)
print(rand_color)

# shuffle(): Toma una lista y la ordena de forma aleatoria.
nombres = ['Andrea', 'Carla', 'Natalia', 'Tamara', 'Rocío']
shuffle(nombres)
print(nombres)

