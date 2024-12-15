# Herencia: Es cuando una clase hija hereda atributos y médotos de una clase padre.
#           Sirve cuando clases se parecen entre si, pero cada una tienen ciertas particularidades.
# 
#  Las clases y la herencia ayudan a no repetir código de forma innecesaria, dado que entre más código 
#  repetido, más dificulta su futura modificación. Esto viene del concepto DRY (Don't repeat yourself).

class Animal:
    
    # Atributo
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    # Método
    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(10, 'amarillo')

piolin.nacer()

print(piolin.color)


# Ejercicios

# Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. 
# Crea otra clase, Alumno, que herede de la primera estos atributos.

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: 
# edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.

class Mascota():

    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

perro = Perro(2,"Lobo",4)

print(perro.edad)


# Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() 
# (puedes dejar el código de los métodos en blanco con pass). 
# Crea una clase llamada Automovil que herede estos métodos de Vehiculo.

class Vehiculo:

    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass