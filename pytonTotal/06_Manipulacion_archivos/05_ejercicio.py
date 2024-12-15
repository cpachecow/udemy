# Maniputación de archivos:
#  La función open abre los archivos y para poderlos leerm hay que añadir:
#   read(), readline() o readlines()

# readlines() lee todo el archivo y lo guarda en una lista. No recomendado para archivos muy grandes.

mi_archivo = open("01_prueba.txt")

lectura_archivo = mi_archivo.readlines() # una forma de leer todas las líneas, quedando en una listas
print(lectura_archivo) # imprimiendo por pantalla la lectura del archivo

mi_archivo.close()
