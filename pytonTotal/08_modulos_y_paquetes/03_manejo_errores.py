# Los manejos de errores se utilizan en Python para que cuando ocurran
# el código pueda aletar del error y seguir funcionando.
# Se utiliza la palabra 'try' para realizar un pedazo de código y
# 'except' se usa para cuando suceda el error hacer o imprimir un mensaje.
# opcionalmente se utiliza un 'else' para hacer algo adicional si el código
# de 'try' sale ok, y 'finaly' se ejecuta si o si finalizando el manejo de error.

def suma():
    num1 = int(input("Ingresa primer numero: "))
    num2 = int(input("Ingresa segundo numero: "))

    print( num1 + num2)

# Al llamar a la funcion suma, esta sumará dos numeros solicitados por pantalla
# en caso que agregue cualquier caracter, este me arrojará un ValueError
# Por lo tanto manejaremos dicho error
try:
    suma()
except ValueError:
    # solo se ejecuta si el error es del tipo ValueError
    print("Ese no es un número")
else:
    # solo se ejecuta si no hay error en 'try'
    print("Suma realizada bien")
finally:
    # siempre se ejecuta
    print(" -- fin -- ")


# Ejemplo con un bucle

def pedir_numero():

    while True:
        try:
            numero = int(input("Deme un número: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Ingresaste el número: {numero}")
            break

pedir_numero()


# Ejercicios

# Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. 
# En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta 
# para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario, 
# verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.
# 
# Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, 
# imprima en pantalla el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el 
# resultado de la suma entre los dos números.

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""

def adicion(num1,num2):
    try: 
        resultado = num1+num2

    except:
        print("Error inesperado")
    else:
        print(num1+num2)

adicion(1,'h')


# Implementa para la siguiente función cociente(), un manejador de errores:
# Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"
# Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo 
# argumento no debe ser cero"
# En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división) 
# entre los dos números entregados como argumento.

def cociente(num1,num2):

    try:
        resultado = num1/num2
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        print(num1/num2)
    
cociente(1,0)


# Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():
# En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), 
# mostrar en pantalla el mensaje: "El archivo no fue encontrado"
# En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"
# Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"
# En todos los casos, al finalizar, imprimir: "Finalizando ejecución"

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

abrir_archivo("hola.txt")