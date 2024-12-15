# Comandos utilizados para:
#  pass: Al iniciar un bucle sin saber su contenido, utilizado para que el flujo del programa siga sin arrojas error.
#  break: Utilizado para salir del bucle en caso que se requiera.
#  continue: Utilizado para salir del bucle en caso de una condición

nombre = 'Cristian'

for i in nombre:
    pass # Aun no se lo que voy agregar, con pass no da error.

for i in nombre:
    if i == 's':
        print('Saliendo del for')
        break # Si se cumple la condición anterior salgo del bucle
    print(i)
print('\n')

for i in nombre:
    if i == 's':
        print('Saliendo del for y continuando')
        continue # Si se cumple la condición anterior salgo del bucle, y vuelvo a ingresar.
    print(i)