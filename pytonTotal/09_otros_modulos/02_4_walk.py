import os

# os.walk(): es un método de os, que permite construir un arbol de una ruta, indicando directorios, subdirectorios y archivos.

ruta = '/home/cpachecow/workspaces/estudio/pyhton/udemy/pytonTotal/09_otros_modulos/ejemplosTxt'

print('\n')
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En el directorio: {carpeta}')
    print(f'Las subcarpetas son: ')
    for subc in subcarpeta:
        print(f'\t{subc}')
    print('Los archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')