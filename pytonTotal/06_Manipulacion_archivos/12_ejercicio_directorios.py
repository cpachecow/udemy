from pathlib import Path

# Con el objeto Path podremos ir a una nueva carpeta
directorio = Path('/home/cpachecow/workspaces/estudio/pyhton/udemy/pytonTotal/03_textos')
archivo = directorio / 'ejemplo01.py' # nueva forma de concatenar un directorio con archivo

mi_archivo = open(archivo)

print('\n//////// Leyendo archivo ////////\n')
print(mi_archivo.read())
print('\n////////////////////////////////\n')