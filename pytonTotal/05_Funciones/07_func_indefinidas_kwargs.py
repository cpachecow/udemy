# **kwargs: Los argumentos con palabras clave (keyword arguments,
# abreviado kwargs), sirven para identificar el argumento por su
# nombre, independientemente de la posición en la que se
# pasen a su función. Si no se conoce de antemano su cantidad,
# se utiliza el parámetro **kwargs que los agrupa en un diccionario.

def prueba(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

prueba(x=1,y=2,z=3,w=4)
print('\n')

def suma(**kwargs):
    suma = 0
    for clave, valor in kwargs.items():
        suma += valor
    return suma

s = suma(x=200, y=300, z=400)
print(s)
print('\n')

def prueba2(num1,num2,*args,**kwargs):
    print(f'Argumento 1: {num1}')
    print(f'Argumento 2: {num2}')

    for i in args:
        print(f'* args: {i}')
    for clave, valor in kwargs.items():
        print(f'** kwargs: {valor}')
prueba2(200,100,10,20,30,x=2000,y=2000)
print('\n')

args = ['sol','luna','estrella']
kwargs = {'c1':111, 'c2':222, 'c3':333}
prueba2('hola', 'mundo', *args,**kwargs) #args y kwargs toma el valor de las variables con los mismos argumentos.

# Crea una función llamada cantidad_atributos que cuente la cantidad de parámetros que se entregan
# , y devuelva esa cantidad como resultado.
def cantidad_atributos(**kwargs):
    contador = 0
    for clave,valor in kwargs.items():
        contador += 1
    return contador

c=cantidad_atributos(x=1,y=2,z=3,k=4,c=1)
print(c)
print('\n')

# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos
#  entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de
#  argumentos de este tipo.

def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(valor)
    return lista
kwargs = {'c1':10, 'c2':20, 'c3':30, 'c4':'HoLa MuNdO'}
g = lista_atributos(**kwargs)
print(g)
print('\n')

# Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida
# de argumentos. Esta función deberá mostrar en pantalla:
#     Características de {nombre}:
#     {nombre_argumento}: {valor_argumento}
#     {nombre_argumento}: {valor_argumento}
#     etc...
# Por ejemplo: describir_persona("María", color_ojos="azules", color_pelo="rubio")#
# Mostrará en pantalla:#
#     Características de María:
#     color_ojos: azules
#     color_pelo: rubio
def describir_personas(nombre,**kwargs):
    print(f'Características de {nombre}')
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')
nombre = 'Eduardo'
kwargs = {'color_ojos':'Marron', 'color_pelo':'Castaño','Estatura':'1,7 mt','nacionalidad':'chileno','edad':'18'}
describir_personas(nombre, **kwargs)