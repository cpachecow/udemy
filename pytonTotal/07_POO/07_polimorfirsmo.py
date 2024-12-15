# Polimorfismo: La palabra está compuesta de 'poli' que significa 'muchos' y 'morfismo' que significa 'formas'.
#               Aplicado a Python se refiere que un mismo método puede ser utilizado en diferentes objetos,
#               obteniendo resultados.

class Vaca:
    
    # Atributos
    def __init__(self, nombre):
        self.nombre = nombre

    # Métodos
    def hablar(self):
        print(f"{self.nombre} dice muuu")

class Oveja:

    # Atributos
    def __init__(self, nombre):
        self.nombre = nombre

    # Métodos
    def hablar(self):
        print(f"{self.nombre} dice beee")

# Instanciado
vaca1 = Vaca("Anita")
oveja1 = Oveja("Priscila")

# El mismo método 'hablar()' es utilizado en dos objetos distintos teniendo resultados diferentes sin arrojar error.
vaca1.hablar()
oveja1.hablar()

# Polimorfismo con una iteración
animales = [vaca1, oveja1]

for animal in animales:
    # Para una misma lista, pero con objetos != el método 'hablar()' arroja distintos resultados
    animal.hablar()


# Polimorfismo con una función
#  Para la misma función y llamando != objetos el resultado de la función cambia, dado el mismo método.

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)

# Ejercicios

# La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto 
# en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.

# Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno 
# de ellos su longitud con la función len(). Puedes recordar cómo implementar la función len() 
# siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

objetos = [palabra, lista, tupla]

for objeto in objetos:
    print(f"{len(objeto)}")



# Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.
# Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, 
# llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases 
# anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

arquero1 = Arquero()
mago1 = Mago()
samurai1 = Samurai()

personajes = [arquero1, mago1, samurai1]

for personaje in personajes:
    personaje.atacar()



# Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.
# Crea una función llamada personaje_defender(), que pueda recibir un objeto 
# (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente 
# de qué tipo de personaje se trate.

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()

def personaje_defender(personaje):
    personaje.defender()

personaje_defender(mago1)
personaje_defender(arquero1)
personaje_defender(samurai1)