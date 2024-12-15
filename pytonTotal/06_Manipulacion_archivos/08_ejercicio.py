# Maniputación de archivos:
#  La función open abre los archivos y tiene dos parámetros, el primero es indicar el archivo y 
#   el segundo indica si es lectura ('r'), escritura ('w') reemplazando el contenido actual de ese archivo
#   y si no existe, lo crea y añade el texto indicado. Por último el parámetro de añadir un texto al final
#   ('a').

archivo = open("02_prueba.txt", 'w')

# Como el archivo existe sobreescribirá el contenido anterior
archivo.write('May the fourth be with you!\n') 

archivo.close()