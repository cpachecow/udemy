# Maniputación de archivos:
#  La función open abre los archivos y para poderlos leerm hay que añadir:
#   read(), readline() o readlines()

# Como son strings, se pueden manipular como tal. Aplicar métodos como upper, strip, etc.


mi_archivo = open("01_prueba.txt")

# print(mi_archivo) > Solo imprime el tipo de metodo

lectura_archivo = mi_archivo.readline() # una forma de leer la primera línea del archivo
print(lectura_archivo.upper()) # toda la línea en mayuscula

lectura_archivo = mi_archivo.readline() # una forma de leer la segunda línea del archivo
print(lectura_archivo.strip()) # línea sin espacio en blanco.

lectura_archivo = mi_archivo.readline() # una forma de leer la tercera línea del archivo
print(lectura_archivo.lower()) # toda la línea en minúscula.

mi_archivo.close()
