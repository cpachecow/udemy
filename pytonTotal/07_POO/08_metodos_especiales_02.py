# Métodos especiales: Llamados también métodos mágicos o dundermethods (del inglés: dunder = double underscore, 
#                     o doble guiónbajo). Pueden ayudarnos a sobrescribir métodos incorporados de Python 
#                     sobre nuestras clases para controlar el resultado devuelto.

class CD:

    # Atributos
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # Métodos especiales

    # Método especial __str__ : para una instancia agregará lo que tenga el método especial'__str__'
    def __str__(self):
        return (f"Autor: {self.autor}, álbum: {self.titulo}")
    
    # Método especial __len__ : puedo devolver la cantidad de canciones del objeto CD
    def __len__(self):
        return self.canciones
    
    # Método especial __del__ : puedo devolver un print una vez utilizado el método
    def __del__(self):
        print(f"Se ha eliminado el CD '{self.titulo}' de '{self.autor}'")


mi_cd = CD("Porcupine Tree", "Closure/Continuation", 10)

# Ahora si se utiliza el método 'str' a la instancia 'mi_cd', mostrará lo indicado en el método especial
# definido __str__.
print(str(mi_cd))

# Si se uitiza 'len' sin usar el método especial asociado, pasará lo siguiente:
# print(len(mi_cd))
# Arrojará un error > TypeError: object of type 'CD' has no len()

# Por lo tanto se puede añadir un método especial para len, para que no arroje dicho error.
print(len(mi_cd))


# Método del elimina en este caso la instancia 'mi_cd', por lo tanto si la quiero utilizar nuevamente
# no se podrá.
# Adicionalmente como fue agregado como método especial __del__, imprime un mensaje al eliminar la instancia.
del mi_cd

# Se puede trabajar con más métodos especiales e investigar cómo se pueden manipular, basta con tipear
# la instancia 'mi_cd.' y saldrán más métodos para poder modificarlos en su resultado final, para crearlos
# como métodos especuales.

# Ejercicios

# Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, 
# devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return (f'"{self.titulo}", de {self.autor}')

mi_libro = Libro('Las Crónicas de Narnia','C.S. Lewis',450)

print(str(mi_libro))


# Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute la función len()
# sobre el mismo, devuelva el número de páginas como número entero.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

mi_libro = Libro('El Señor de Los Anillos','J.R.R. Tolkien', 1020)

print(len(mi_libro))


# Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje 
# "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")

mi_libro = Libro('El Arte de Amar','Erich Fromm', 145)

del(mi_libro)