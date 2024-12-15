# Las funciones indefinidas (*agrs) permiten pasar un numero variable de parámetros
# *args significa literalmente todos los argumentos.
def suma(*args):
    return sum(args)

s = suma(10,20,30,5) # independiente de la cantidad de parámetros, la suma se realizará
print(s)

# Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos,
# y que retorne la suma de sus valores al cuadrado.
def suma_cuadrados(*args):
    suma = 0
    for i in args:
        suma += i**2
    return suma

s2 = suma_cuadrados(1,2,3,4)
print(s2)

# Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier
# extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume,
# o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*args):
    suma = 0
    for i in args:
        suma += abs(i)
    return suma

s3 = suma_absolutos(-1,-2,-3,4,-5)
print(s3)

# Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación,
# una cantidad indefinida de números. La función debe devolver el siguiente mensaje:
#  "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre,*args):
    suma = sum(args)
    mensaje = f'{nombre}, la suma de tus números es {suma}'
    return mensaje

nombre = input('Favor indicar nombre: ')
msj = numeros_persona(nombre,5,3,3)
print(msj)

