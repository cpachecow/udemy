# Maniputación de archivos:
#  La función open abre los archivos y tiene dos parámetros, el primero es indicar el archivo y 
#   el segundo indica si es lectura ('r'), escritura ('w') reemplazando el contenido actual de ese archivo
#   y si no existe, lo crea y añade el texto indicado. Por último el parámetro de añadir un texto al final
#   ('a').

archivo = open("01_prueba.txt", 'r')

archivo.write('Hola mundo!') # Arrojará un error dado que el archivo se abrió con el modo solo lectura.

archivo.close()