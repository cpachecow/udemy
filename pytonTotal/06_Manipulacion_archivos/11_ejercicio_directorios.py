import os

# Metodo getcwd(): Indica la ruta actual de directorio.
ruta = os.getcwd()

print(f'La ruta de directorio actual es: {ruta}')

# Metodo chdir(): Modifica el directorio actual, permitiendo abrir archivos en otras direcciones.
os.chdir('../03_textos/')

archivo = open('ejemplo01.py')

print(archivo.read())

# Metodo makedirs(): Crea un nuevo directorio en la ruta actual.
# nuevo_directorio = os.makedirs('crear_dir')

# Medoto rmdir(): Elimina un directorio de la ruta actual
# os.rmdir('crear_dir')
# Si no encuentra nada, arrojará error.