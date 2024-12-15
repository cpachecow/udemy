# Maniputación de archivos:
#  La función open abre los archivos y tiene dos parámetros, el primero es indicar el archivo y 
#   el segundo indica si es lectura ('r'), escritura ('w') reemplazando el contenido actual de ese archivo
#   y si no existe, lo crea y añade el texto indicado. Por último el parámetro de añadir un texto al final
#   ('a').

archivo = open("02_prueba.txt", 'w')

archivo.write('Hola mundo!') # Si el archivo no existe lo creará y escribirá el contenido indicado.

# Como el archivo ya existe, escribirá a continuación los contenidos write() a continuación.
#   Si en un nuevo archivo de Python ejecuto la funcion open con el parámetro w y escribo con write,
#   todo su contenido anterior se borrará y se escribirá lo que escriba en ese momento.
archivo.write('Hola soy un chanchito 01!') 

archivo.write('Hola soy un chanchito 02!') 
archivo.write('Hola soy un chanchito 03!') 
archivo.write('Hola soy un chanchito 04!') 


archivo.close()