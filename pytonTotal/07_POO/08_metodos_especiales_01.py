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


mi_cd = CD("Porcupine Tree", "Closure/Continuario", 10)

# Imprimirá por pantalla la instancia del objeto CD y dónde se alojó en memoria
print(mi_cd)

# Ahora si se utiliza el método 'str' a la instancia 'mi_cd', hará exactamente lo mismo.
print(str(mi_cd))

