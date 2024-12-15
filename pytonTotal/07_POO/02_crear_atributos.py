# Atributos: Son las características de las clases. O variables que pertenecen a la clase.
#  Pueden ser del tipo:
#   1.- Atributos de clase: Indicarán las características de todas las instancias de la clase.
#   2.- Atributos de instancia o al objeto: puede ser diferente de cada objeto, ejemplo colores de un pájaro.

class Pajaro:
    
    # Atriburo de clase
    alas = True

    # Atriburo de instancia, self.color que obedece al parámetro color, self.tamanio al parámetro tamanio
    def __init__(self, color, tamanio):
        self.color = color
        self.tamanio = tamanio

# Instancia pajaro_01
parajo_01 = Pajaro('café', '21 cm')

print(parajo_01.color)
print(parajo_01.tamanio)
print(parajo_01.alas)
print("\n")

# Instancia pajaro_02
parajo_02 = Pajaro('negro', '40 cm')

print(parajo_02.color)
print(parajo_02.tamanio)
print(parajo_02.alas)
print("\n")

class Cubo:
    caras = 6
    
    def __init__(self,color):
        self.color = color

cubo_rojo = Cubo("rojo")
print(cubo_rojo.color)
print("\n")

# Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
#  real = False
# Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
#  especie = "Humano"
#  magico = True
#  edad = 17

class Personaje:
    real = False
    
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", True, 17)

print(harry_potter.edad)