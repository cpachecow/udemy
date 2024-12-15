# Generadores
#  Tipo especial de funciones que devuelven un iterador que almacena su contenido a medida que se solicita.

# Ejemplo 1
def secuencia_infinita():
    num = 0
    while True:
        yield num
        num +=1

generador = secuencia_infinita()

# Con next voy llamando al valor asignado en la iteración, a medida que se va llamando nuevamente genera 
# el proximo valor.
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

print("\n")

# Ejemplo 2
def mi_generador():
    for x in range(1, 5):
        yield x * 10

g = mi_generador()

print(next(g))
print(next(g))
print("\n")

# Ejemplo 3

def mi_generador2():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador2()
print(next(g))
print(next(g))
print("\n")

# Crea un generador (almacenado en la variable generador) que sea capaz de devolver 
# una secuencia infinita de números, iniciando desde el 1, y entregando un número 
# consecutivo superior cada vez que sea llamada mediante next.

def secuencia_infinita():
    num = 1
    while True:
        yield num
        num +=1

generador = secuencia_infinita()
print(next(generador))
print("\n")

# Crea un generador (almacenado en la variable generador) que sea capaz de devolver
# de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez 
# que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def secuencia_infinita():
    num = 1
    const = 7
    while True:
        yield const * num
        num += 1

generador = secuencia_infinita()
print(next(generador))
print(next(generador))
print(next(generador))
print("\n")

# Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva 
# un mensaje cada vez que sea llamado:
# "Te quedan 3 vidas"
# "Te quedan 2 vidas"
# "Te queda 1 vida"
# "Game Over"
# Almacena el generador en la variable perder_vida

def vidas():
    vidas = 3
    while True:
        yield vidas
        vidas -= 1

perder_vida = vidas()
print(f"Te quedan {next(perder_vida)} vidas")
print(f"Te quedan {next(perder_vida)} vidas")
print(f"Te quedan {next(perder_vida)} vidas")
print("Game Over")
