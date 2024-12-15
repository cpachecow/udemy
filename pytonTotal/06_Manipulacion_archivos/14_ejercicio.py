from pathlib import Path

# El objeto path, construye desde una lista de caracteres y otros objetos, una ruta de directorio
guia = Path("España", "Barcelona", "La_casa_del_tibet.txt")
print(guia)

# El método Path.home() indica la ruta home que variará según SO
base = Path.home()
print("\n- El home es: ")
print(base)

# Se crea una ruta absoluta, que combina el home y una ruta interna.
guia2 = Path(base,guia)
print("\n- La ruta absoluta es: ")
print(guia2)

# El método with_name("archivo.txt"): toma la ruta asociando un path anterior o seleccionado y conserva 
#                                     la ruta eligiendo otro archivo, por ejemplo.
guia3 = guia2.with_name("La_plaza_de_toros.txt")
print(guia3)

# El atributo parent: devuelve el antecesor de la ruta actual
print(guia3.parent) # Debería volver 'Barcelona'
print(guia3.parent.parent) # Debería volver 'España'
