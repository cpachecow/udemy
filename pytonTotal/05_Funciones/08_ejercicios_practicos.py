# Ejercicio 01:
#  Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
#   Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
#   Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
#   Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio.
def devolver_distintos(x,y,z):
    suma = x + y + z
    lista = [x,y,z]
    if(suma > 15):
        return max(x,y,z)
    elif(suma < 10):
        return min(x,y,z)
    elif((suma >= 10) and (suma <= 15)):
        lista.sort()
        return lista[1]

print(devolver_distintos(1,10,2))

# Ejercicio 02: Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como
# parámetro, y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']

def transforma_palabra(palabra):
    texto = set([])
    for i in palabra:
        texto.add(i)

    texto = list(texto)
    texto.sort()

    return texto

print(transforma_palabra('entretenido'))

# Ejercicio 03
# Escribe una función que requiera una cantidad indefinida de # argumentos. Lo que hará esta función es devolver
# True si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas. Por ejemplo:
#   (5,6,1,0,0,9,3,5) >>> True
#   (6,0,5,1,0,3,0,1) >>> False
def ceros_repetidos(*args):
    posicion = 0
    cero = 0
    largo_cadena = len(args)
    
    if largo_cadena >= 2:
        for num in args:
            if(num == 0):
                cero += 1
                if(cero == 2): #Se detecta el segundo cero de la lista
                    posicion += 1 #Registramos la posicion del segundo cero
                    break
            posicion += 1

        # si la posición del segundo cero encontrado menos su posición anterior es igual a cero, indica true.
        if((args[posicion-1]==0) and (args[posicion-2] == 0)):
            return True
        else:
            return False
    else:
        return False

print(ceros_repetidos(1,0,1,0,1)) #encuentra dos ceros consecutivos y devuelve true
print('\n')

# Ejercicio 04
# Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
# Esta función va a mostrar en pantalla cuántos números primos hay en el rango que va desde cero hasta ese número
# incluido, y va a devolver la cantidad de números primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.

def contar_primos(*args):

    contador = 0
    primos = []

    for i in args:
        if(i > 1):
            #print(f'###### i: {i}')
            for j in range(2,i):
                #print(f'{range(2,i)} i:{i} % j:{j} resto = {i%j}')
                if (i % j == 0):
                    #print('break')
                    break
            else:
                contador += 1
                primos.append(i)
    return f'Total números primos: {contador} \nListado de numeros primos encontrados: {primos}'

# f = contar_primos(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131)
f = contar_primos(6,1,3,5,0,2,8,2)
print(f'\n{f}')
