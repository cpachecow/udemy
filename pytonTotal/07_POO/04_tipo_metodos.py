# Métodos de instacia: Son las funciones de una clase.
#                      Son los que vieron en la sesion anterior y tienen como característica:
#                        1.- Se puede acceder a los otros métodos y atributos de la clase.
#                        2.- Se puede modificar un atributo de la clase.
#                        3.- Se puede modificar el estado de una clase.
#                        4.- Acepta como parámetro 'self'.
#
# Métodos de clase: Que se ocupa mencionando el decorador @classmetohd.
#                        1.- No pueden acceder a los atributos de instancia.
#                        2.- Pueden modificar los atributos de la clase.
#                        3.- Acepta como parámetro 'cls' em vez de 'self'.
#                             Ejemplo:
#                               @classmethod
#                               def cantidad_patas(cls,cantidad)
#                               print(f"Este animal tiene {cantidad} patas")
#
# Métodos estáticos: Que se ocupa mencionando el decorador @staticmetohd.
#                        1.- No aceptan como parámetro ni 'self' ni 'cls'.
#                        2.- No se puede modificar estados de la clase ni de la instancia.
#                        3.- Acpetan parámetros de entrada.
#                             Ejemplo:
#                               @staticmethod
#                               def hola_nombre(nombre)
#                               print(f"hola {nombre}, bienvenido(a)!")

class Pajaro:
    
    # Atriburo de clase
    alas = True
    ojos = 2

    # Atriburo de instancia, self.color que obedece al parámetro color, self.especie al parámetro especie
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    # Métodos de instancia

    def piar(self):
        # 1.- Puedo acceder a un atributo de la clase la palabra self.nombre_del_atributo
        print(f"Pío-Pío, mi color es {self.color}")
    
    # Este método contiene un parámetro llamado metros
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        # Puedo acceder a otros métodos de la clase
        self.piar()

    # 2.- Puedo modificar un atributo de la instancia
    def cambia_color(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es de color {self.color}")
    
    # Método de clase: solo puede acceder a los atributos de la clase, no a los de instancia, 
    #                  ni a los métodos de instancia. Para crearlos debe tener def(cls,nombre_parametro):
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.ojos = 1
        print(f"El pajaro tiene {cls.ojos} ojo(s)")

    # Método estáticos: No puede acceder a los atributos de la clase, no a los de instancia, 
    #                   ni a los métodos de instancia. Por lo tanto no pueden modificar sus estados.
    @staticmethod
    def mirar():
        print("El pajaro mira")

piolin = Pajaro('Amarillo', 'Canario')

piolin.cambia_color()

# 3.- Puedo modificar un atributo de la clase Pájaro
piolin.alas = False
print(f"Mi pájaro tiene alas: {piolin.alas}")

# Método de clase, no necesitan ser instanciado para poder ejecutarse.
Pajaro.poner_huevos(3)

# Método estático, no necesitan ser instanciado para poder ejecutarse.
Pajaro.mirar()


# Práctica Tipos de Métodos 

# Crea un método estático respirar() para la clase Mascota. 
# Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"

class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
    
Mascota.respirar()

# Crea un método de clase revivir() que actúa sobre 
#  el atributo de clase vivo de la clase Jugador, 
#  estableciéndolo en True cada vez que es invocado. 
#  El valor predeterminado del atributo vivo, debe ser False.

class Jugador:

    vivo = False
    
    @classmethod
    def revivir(cls, vivo = True):
        cls.vivo = vivo
        print(cls.vivo)

Jugador.revivir(True)

# Crea un método de instancia lanzar_flecha() 
# que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, 
# que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.

class Personaje:
    cantidad_flechas = 10

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        print(self.cantidad_flechas)

        # if flechas_disponibles >= 0:
        #     print(f"flecha(s) lanzada(a): {cantidad_flechas}, flechas disponibles: {flechas_disponibles}")
        # else:
        #     print(f" La cantidad de flecha(s) lanzada(a): {cantidad_flechas}, no puede ser mayor a flechas disponibles: {self.cantidad_flechas}")

indio = Personaje()

indio.lanzar_flecha()