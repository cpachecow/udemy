# Maniputación de archivos:
#  La función open abre los archivos y para poderlos leerm hay que añadir:
#   read(), readline() o readlines()

#   readline(): Se utiliza para leer una línea de un archivo.

mi_archivo = open("01_prueba.txt")

# print(mi_archivo) > Solo imprime el tipo de metodo

lectura_archivo = mi_archivo.readline() # Se guarda el contenido de la primera línea del archivo.
print(lectura_archivo) # para luego poder imprimir.

lectura_archivo = mi_archivo.readline() # Se guarda el contenido de la segunda línea del archivo
print(lectura_archivo) # para luego poder imprimir.

lectura_archivo = mi_archivo.readline() # Se guarda el contenido de la tercera línea del archivo
print(lectura_archivo) # para luego poder imprimir.

mi_archivo.close()
