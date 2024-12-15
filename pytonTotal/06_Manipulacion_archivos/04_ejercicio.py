# Maniputación de archivos:
#  La función open abre los archivos y para poderlos leer hay que añadir:
#   read(), readline() o readlines()

mi_archivo = open("01_prueba.txt")

# Se puede recorrer el archivo con un for
for i in mi_archivo:
    print("Esta línea dice: " + i)

mi_archivo.close()
