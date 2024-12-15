import os
import shutil
import send2trash

# Nos indicará la ruta actual donde estamos
print(os.getcwd())

# crear archivo, ingresar informacion y cerrarlo
archivo = open('02_ejemplo.txt','w')
archivo.write('texto de prueba')
archivo.close()

# Indicará en una lista, el contenido del directorio con sus archivos
print(os.listdir())
