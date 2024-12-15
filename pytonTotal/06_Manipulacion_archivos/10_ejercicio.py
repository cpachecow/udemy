# Maniputación de archivos:
#  La función open abre los archivos y tiene dos parámetros, el primero es indicar el archivo y 
#   el segundo indica si es lectura ('r'), escritura ('w') reemplazando el contenido actual de ese archivo
#   y si no existe, lo crea y añade el texto indicado. Por último el parámetro de añadir un texto al final
#   ('a').

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open("10_registro.txt", 'w')

for i in registro_ultima_sesion:
    archivo.write(i+'\t')

archivo.close()

archivo = open("10_registro.txt", 'r')

print(archivo.read())

archivo.close()