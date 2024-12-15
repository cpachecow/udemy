# Herencia: La clase hija va a heredar todos los atributos y metodos de la clase padre (o las que se agreguen adicionalmente). 
#           Si una clase hija tiene un método del mismo nombre, dará prioridad a su método.

class Padre:
    
    def saludo(self):
        print("Hola, yo soy el padre!")

class Madre:
    def reir(self):
        print("jua jua jua")

    def saludo(self):
        print("Hola, yo soy el madre!")

class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()


# Método heredado de la clase Padre, para que el saludo sea el de la Madre, se tendrá que invertir el orden de la herencia
# class Hijo(Madre,Padre):

mi_nieto.saludo()

# Método heredado de la clase Madre
mi_nieto.reir()

# Propiedad especial '___mro___' que indicará como buscará los métodos de una clase que ha herenciado de otras.
# Priorizará de izquierda a derecha. Para este ejemplo buscará primero en Nieto > Hijo > Padre > Madre
# La razón por qué el saludo es del Padre, porque lo hereda primero que la madre.
print(Nieto.__mro__)

# Ejercicios

# Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, 
# y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita 
# a esta clase heredar correctamente de Padre y Madre.
# Completa el código suministrado a continuación para lograrlo.

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre, Padre):
    pass

mi_hija = Hija()

mi_hija.reir()
mi_hija.trabajar()


# "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; 
# y amamanta a sus crías pero no tienen mamas." (National Geographic) 
# Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, 
# tal que "construyas" un animal que tiene los siguientes métodos y atributos:
# - poner_huevos() 
# - tiene_pico = True
# - vertebrado = True
# - venenoso = True
# - nadar()
# - caminar()
# - amamantar()

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave, Vertebrado):
    pass

mi_ornitorrinco = Ornitorrinco()


# Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. 
# Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo 
# el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):

    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
    
mi_hijo = Hijo()

# >> Mostrará el método hobby de la clase Hijo, dado que primero busca en su clase, y después en sus herederos.
print(mi_hijo.hobby()) 