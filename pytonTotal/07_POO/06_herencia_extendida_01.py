# Herencia: La clase hija va a heredar todos los atributos y metodos de la clase padre. 
#           Pero se una clase hija tiene un método del mismo nombre, dará prioridad a su método.

class Animal:
    
    # Atributos
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    # Métodos
    def nacer(self):
        print("Este animal ha nacido")
    
    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    
    # Para agregar un atributo, tengo dos opciones:

    # 1.- Agregar los mismos atributos de su clase padre y agregar los propios,
    #     para el ejemplo se agrega 'altura_vuelo'.
    def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo # -> agregar esta línea

    # 2.- Se agrega los mismos atributos de la opción anterior, pero para no 
    #     estar copiando nuevamente las líneas 'self.edad = edad' y 'self.color = color'
    #     se agrega la línea 'super().__init__(edad,color)', que hereda los atributos de la 
    #     clase padre y solo habría que agregar el o los atributos de la clase hijo.
    # def __init__(self, edad, color, altura_vuelo):
    #     super().__init__(edad,color) # -> agregar esta línea, para heredar los atributos de la clase padre
    #     self.altura_vuelo = altura_vuelo # -> agregar esta línea


    def hablar(self):
        print("Pío")

    # Método que existe en esta clase, y no en su clase Padre.
    def volar(self, metros):
        print(f"el pajaro vuela {metros} metros")

piolin = Pajaro(3,'amarillo',10)

# Metodo heredado de su clase padre
piolin.nacer()

# Metodo heredado de su clase padre, pero como también tiene un método con el mismo nombre
# priorizará sus propios métodos.
piolin.hablar()

piolin.volar(2)

print(piolin.altura_vuelo)