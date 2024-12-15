# DICCIONARIOS

# Son objetos que están compuestos por una única clave y un valor

# Estructura básica
dic = {'c1':123456, 'c2':'Om Ah Jung', 'c3':'Esto es una prueba'}
print("El objeto es de tipo: ", type(dic))
print(dic)

# Obtener un valor del Diccionario
result = dic['c3']
print(result)

# El Diccionario puede tener cualquier tipo de datos, listas, tuplas y diccionarios.
dic2 = {'c1':123456, 'c2':{'d1':'hola','d2':'chao'}, 'c3':(1,'dos',3), 'c4':[4,'cinco',6,'siete']}
print(dic2)
result2 = dic2['c4']
print(type(result2))

dic3 = {'c1':['a','b','c'], 'c2':['d','e','f']}
result3 = dic3['c2'][1] # De la segunda llave del dicc, obtenemos el tercer valor de la lista.
print(result3.upper()) # Se toma el valor y se deja en mayuscula.

# Agregar contenido al dicc
dic4 = {1:'a', 2:'b'}
dic4['cc'] = 'hola' # Se puede agregar cualquier llave que no esté anteriormente.
print(dic4)

# Sobrescribir un diccionario
dic4['cc'] = 'c'
print(dic4)

# Para obtener las llaves de un dicc
print("Llaves de diccionario: ", dic4.keys())

# Para obtener los valores de un dicc
print("Valores de diccionario: ", dic4.values())

# Para obtener todo el contenido de un dicc
print("Todo el diccionario: ", dic4.items())
