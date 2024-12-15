# Módulo Collections nos ayuda a completar y a manipular las estructuras de datos 
# (listas, tuplas, diccionarios, etc) de una manera eficiente.

from collections import defaultdict

# ------------
# defaultdict: Nos devolverá una llave y valor por defecto de un diccionario, en caso que la llave 
#              no se encuentre.
# ------------

myDic = {'uno':'verde','dos':'azul','tres':'rojo'}
print(myDic['uno']) # En este caso la llave 'uno' existe, por lo tanto devuelve el valor verde.

# print(myDic['cuatro']) > En este caso la llave 'cuatro' no existe, por lo tanto arroja error 'KeyError'.

# La clase defauldict da un valor por defecto, para las llaves no existentes de un diccionario
myDic = defaultdict(lambda: 'no existe')

# Por lo tanto al solicitar el valor de la llave 'cuatro' , al no existir toma el valor por defecto 'no existe'
print(myDic['cuatro'])
