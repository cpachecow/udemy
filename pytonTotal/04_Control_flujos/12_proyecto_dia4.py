from random import randint
# Proyecto día 4: Adivina el número
#  1.- Preguntar nombre
#  2.- Usuario debe adivinar número entre 1 y el 100, tiene 8 intentos.
#  3.- Si el número es menor a uno o mayor a 100, se debe informar.
#  4.- Si el número es menor al que tiene pensado por el programa, debe informar.
#  5.- Si el número es mayor al que tiene pensado por el programa, debe informar.
#  6.- Si el usuario adivino el número, se debe informar e indicar el número de intentos.
print('*** Bienvenido al Juego que debes adivinar un número del 1 al 100 ***')
print('*** Tiene 8 intentos ***')

# num_correcto = 40 # con esta opción
num_correcto = randint(1,100)
intentos = 8

nombre = input('\nIngrese su nombre: ')

while intentos > 0:
    num = int(input('\nIngrese el número a adivinar: '))
    if num < 1:
        print("Numero debe ser Mayor a 1")
        intentos -= 1
        print(f'Le quedan {intentos} intentos')
        continue
    elif num > 100:
        print("Numero debe ser Menor a 100")
        intentos -= 1
        print(f'Le quedan {intentos} intentos')
        continue
    elif num < num_correcto:
        print("El numero ingresado es *Menor* al numero a adivinar")
        intentos -= 1
        print(f'Le quedan {intentos} intentos')
        continue
    elif num > num_correcto:
        print("El numero ingresado es *Mayor* al numero a adivinar")
        intentos -= 1
        print(f'Le quedan {intentos} intentos')
        continue
    elif num == num_correcto:
        print(f"\n{nombre} haz encontrado el numero, felicitaciones !!!!")
        print(f'Adivinó en el intento: {intentos}')
        break
else :
    print(f'\n&&& Juego terminado :(, El numero elegido era {num_correcto} &&&')