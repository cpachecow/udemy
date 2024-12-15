# Ejercicio como extraer parte de una cadena

texto = "Me encanta programar y aprender"
# Cuando paso la variable texto con dos parámetros, me indica desde dónde
#  hasta dónde voy a estraer la cadena de texto, sin incluir el último numero
extrae = texto[2:10]
print (extrae)

# El tercer parámatro indica cada cuántos caracteres se van a extraer.
extrae = texto[2:10:2]
print (extrae)

# Si dejo un parámetro vacío me indica que tomará toda la cadena en el rango
extrae = texto[3:]
print (extrae)

# Si dejo un parámetro vacío me indica que tomará toda la cadena en el rango
extrae = texto[:3]
print (extrae)

# Si los dos parámetros están vacíos tomará toda la cadena, y si el último parámetro indica cada cuantos
# caracteres extraera y guardará en la variable extrae
extrae = texto[::7]
print (extrae)
