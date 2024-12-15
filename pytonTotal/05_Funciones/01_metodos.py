# La documentación indica los detalles de las funciones de Python.
# Los médotos son las funciones de un objeto, las cuales son muy variadas.
# Se puede buscar información en la página oficial de Phyton, o ejemplos en la web.

# Por ejemplo está la función de lstrip(), que elimina los textos indicados por parámetro en un string.
texto = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'
print(f'Texto original: {texto}')
texto = texto.lstrip(',:_#')
print(f'Texto modificado con lstrip: {texto}')

# Función insert(), añade un texto en una lista con una ubicación específica.
#  Ejemplo: Añadir a la lista frutas, el elemento 'naranja' en la posición 4.
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
print(f'texto original: {frutas}')
frutas.insert(3,'naranja')
print(f'texto modificado con insert(): {frutas}')

# Verifica si los sets a continuación forman conjuntos aislados
#  (es decir, que no tienen elementos en común), utilizando el método isdisjoint().
#  Almacena dicho resultado en la variable conjuntos_aislados:
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)