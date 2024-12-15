from os import system
from pathlib import Path

home = Path.home()
sub_dir = Path("workspaces/estudio/pyhton/udemy/pytonTotal/06_Manipulacion_archivos/docs/proyecto/recetas")

dir = Path(home, sub_dir)

def leer_receta(archivo):
    mi_archivo = open(archivo)
    return mi_archivo.read()

def crear_receta(archivo, contenido):
    archivo = {archivo}+".txt"
    receta = open(archivo, 'w')
    receta.write(contenido)

def crear_categoria(nombre):
    pass

def mostrar_recetas():
    pass

def categorias():
    system('clear')
    
    
    # print("Listado de Categorías: \n")
    d = Path('.')
    a = 0
    b = []
    for x in d.iterdir():
        if x.is_dir():
            b.append(x) 
            a += 1
            print(f"{a}) {x}")
    
    categoria = input("\nSeleccione una de las categorías: \n")

    if categoria == '1':
       i = int(categoria)
       receta_dir = str(b[i-1])
    #    print(receta_dir)
       sub_dir = Path(f"workspaces/estudio/pyhton/udemy/pytonTotal/06_Manipulacion_archivos/docs/proyecto/recetas/{receta_dir}")
    #    sub_dir = sub_dir+"/"+receta_dir
       dir = Path(home, sub_dir)
    #    print(dir2)
       # print(dir2)
    #    d = Path('.')
    #    d = d / receta_dir
    #    print(d)
       for x in Path(dir).glob('*.txt'):
                if x:
                    i += 1
                    print(f"{i}) {x}")

    # receta = input("\nQué receta quiere leer: \n")

    # if receta is not None:
    #     print(x[0])

    files = (x for x in Path(dir).glob('*.txt') if x.is_file())
    for file in files:
        print(str(file), "is a file!")

def esInt(valor):
    try:
        i = int(valor)
        if i <= 0:
            return False
    except:  
        return False
    return True

def bienvenida():
    texto_inicial = "\n /// Querido usuario, te damos la bienvenida al recetario Wolfx ///\n"
    print(texto_inicial)

def despedida():
    system('clear')
    texto_final = "\n *** Saliendo del sistema...  Muchas gracias ***\n"
    print(texto_final)

bienvenida()

print(f"La ruta de acceso es: {dir}\n")

x = 0
for txt in Path(dir).glob('**/*.txt'):
    if txt:
        x += 1        

    else:
        print("No se han encontrado lo que está buscando.")

print(f"Contamos con un total de {x} recetas diponibles")

opcion = '0'
while opcion != '6':    
    opcion = input("""\nSelecione alguna de las siguientes opciones: 
                   
                    1.- Seleccionar categoría de receta y leer receta.
                    2.- Selecionar categoría y crear receta.
                    3.- Crear nueva categoría.
                    4.- Seleccionar categoría de receta y eliminar receta.
                    5.- Favor indicar qué categoría desea eliminar.
                    6.- Salir del programa\n\n""")

    

    if opcion == '1':
        categorias()
        opcion = input("\nPresione cualquier tecla para continuar...  \n")
        system('clear')
    
    if opcion == '6':
        despedida()

# d = Path('.')
# for x in d.iterdir():
#         if x.is_dir():
#             print(x)
    
# print(list(d.glob('/*.txt')))

