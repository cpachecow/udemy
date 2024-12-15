# Métodos: son las funciones de una clase, tiene que tener self, y posterior a eso los parámetros que requiera.

class Pajaro:
    
    # Atriburo de clase
    alas = True

    # Atriburo de instancia, self.color que obedece al parámetro color, self.especie al parámetro especie
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    # Métodos

    def piar(self):
        # puedo pasar un atributo al método anteponiendo la palabra self.nombre_del_atributo
        print(f"Pío-Pío, mi color es {self.color}")
    
    # Este método contiene un parámetro llamado metros
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

piolin = Pajaro('Amarillo', 'Canario')

piolin.piar()
piolin.volar(7)

# Crea una clase Perro. Dicho perro debe poder ladrar.
# # Crea el método ladrar() y ejecútalo en una instancia de Perro. 
# Cada vez que ladre, debe mostrarse en pantalla "Guau!".

class Perro:

    def ladrar(self):
        print("Guau!")

perro = Perro()

perro.ladrar()


# Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
# Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
class Mago:
    
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()

merlin.lanzar_hechizo()


# Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). 
# El método debe imprimir en pantalla el mensaje
# "La alarma ha sido pospuesta {cantidad_minutos} minutos"

class Alarma:

    def postergar(self, cantidad_minutos)->int:
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

tsunami = Alarma()

tsunami.postergar(10)