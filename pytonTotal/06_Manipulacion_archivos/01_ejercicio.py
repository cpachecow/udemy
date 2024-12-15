# Maniputación de archivos:
#  La función open abre los archivos y para poderlos leerm hay que añadir:
#   read(), readline() o readlines()


mi_archivo = open("01_prueba.txt")

# print(mi_archivo) > Solo imprime el tipo de metodo

lectura_archivo = mi_archivo.read() # una forma de leer un archivo

print(lectura_archivo) # para luego poder imprimir.

mi_archivo.close()


mi_archivo = open("01_prueba.txt")
print("Lectura una línea: " + mi_archivo.readline())

print("Lectura una línea: " + mi_archivo.readline())
mi_archivo.close()