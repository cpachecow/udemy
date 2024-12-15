# Crear funcion para abrir y otra para cerrar un archivo

def abre_archivo(archivo):
    mi_archivo = open(archivo)
    return mi_archivo.read()

print(abre_archivo('01_prueba.txt'))

# Crea funcion que abre un archivo y sobreescribe su contenido.
def sobreescribe_archivo(archivo):
    mi_archivo = open(archivo, 'w')
    mi_archivo.write('Contenido eliminado')

sobreescribe_archivo('17_prueba.txt')

print(abre_archivo('17_prueba.txt'))

# Crea una función llamada registro_error() que abra (open) un archivo indicado 
# como parámetro, y lo actualice añadiendo una línea al final que indique 
# "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.

def registro_error(archivo):
    mi_archivo = open(archivo, 'a')
    mi_archivo.write('\nSe ha registrado un error de ejecución')

registro_error('17_prueba.txt')
print(abre_archivo('17_prueba.txt'))
