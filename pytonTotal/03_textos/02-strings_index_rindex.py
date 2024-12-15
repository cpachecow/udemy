# Entendimiento busqueda en strings
# Uso de los métodos index y rindex

texto = "Hola como esta tu familia"

# index() me indicará la posición de la primera 'a' de izq a der
#   también se puede buscar una palabra, e index() me indicará la primera posición
#   de la palabra encontrada.
resultado = texto.index("a") #la primera 'a' del texto anterior está en la posición 3.
print(resultado)

# rindex() me indicará la posición de la primera 'a' de der a izq
resultado = texto.rindex("a") #la primera 'a' del texto anterior está en la posición 24.
print(resultado)

