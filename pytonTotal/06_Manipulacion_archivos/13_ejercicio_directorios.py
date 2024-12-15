from pathlib import Path, PureWindowsPath

# Con el objeto Path podremos ir a una nueva carpeta y también a un archivo especifico
archivo = Path('/home/cpachecow/workspaces/estudio/pyhton/udemy/pytonTotal/03_textos/ejemplo02.py')

print('\n//////// Leyendo archivo ////////\n')

# El método read_text() leemos el archivo indicado en la ruta anterior, 
#  no requiere abrir o cerrar el archivo, porque internamente ya lo realiza.
print(archivo.read_text()) 

print('\n////// Fin lectura archivo /////\n')

# El método name: indica el nombre del archivo, extraido del objeto path.
print(f'\nEl nombre del archivo es: \'{archivo.name}\'\n')

# El método suffix: indica la extesión del archivo abierto.
print(f'\nEl nombre de la extensión es: \'{archivo.suffix}\'\n')

# El método stem: indica el nombre del archivo sin extensión. 
print(f'\nEl nombre del archivo, sin extensión: \'{archivo.stem}\'\n')

# El metodo exist(): indica si el archivo que queremos abrir está o no (es booleano).
if not archivo.exists():
    print('\nArchivo no existe :(\n\n')
else:
    print('\nArchivo encontrado :)\n\n')

ruta_windows = PureWindowsPath(archivo)

print(f'Ruta tipo Windows: {ruta_windows}\n\n')