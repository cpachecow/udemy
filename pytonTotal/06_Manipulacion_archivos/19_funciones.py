def abrir_leer(archivo):
    mi_archivo = open(archivo)
    return mi_archivo.read()

def sobrescribir(archivo, contenido):
    mi_archivo = open(archivo, 'w')
    mi_archivo.write(contenido)

def registro_error(archivo):
    mi_archivo = open(archivo, 'a')
    mi_archivo.write('Se ha registrado un error de ejecución')

print("\n")
print("Lectura archivo 1:")
print(abrir_leer('02_prueba.txt'))

print("Lectura archivo 2:")
contenido = "Chanchito feliz!\n"
sobrescribir('01_prueba.txt', contenido)
print(abrir_leer('01_prueba.txt'))
print("\n")

print("Lectura archivo 1 modificado:")
registro_error('01_prueba.txt')
print(abrir_leer('01_prueba.txt'))
print("\n")