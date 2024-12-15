# Maniputación de archivos:
#  La función open abre los archivos y tiene dos parámetros, el primero es indicar el archivo y 
#   el segundo indica si es lectura ('r'), escritura ('w') reemplazando el contenido actual de ese archivo
#   y si no existe, lo crea y añade el texto indicado. Por último el parámetro de añadir un texto al final
#   ('a').

# Con el parámetro 'a', al realizar una escritura, esta quedará al final del archivo.
archivo = open("02_prueba.txt", 'a')

archivo.write('Este es un texto que quedará al final\n') 

archivo.close()