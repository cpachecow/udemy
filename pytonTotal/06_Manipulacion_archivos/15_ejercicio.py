from pathlib import Path

home = Path.home()

sub_dir = Path("workspaces/estudio/pyhton/udemy/pytonTotal/06_Manipulacion_archivos/docs/Europa")

# Construccion ruta absoluta
dir = Path(home, sub_dir)

print(f'\n{dir}\n')

# Mostrará los archivos con extensión txt encontrados en la carpeta 'Europa'.
for txt in Path(dir).glob('*.txt'):
    if txt:        
        print(txt)
        print('\n')
    else:
        print("No se han encontrado lo que está buscando.")

print('/////////////////////////////////\n\n')

# Mostrará todos los archivos con extensión txt encontrados en la carpeta 'Europa' 
# y dentro de está también buscará.
for txt in Path(dir).glob('**/*.txt'):
    if txt:        
        print(txt)
    else:
        print("No se han encontrado lo que está buscando.")