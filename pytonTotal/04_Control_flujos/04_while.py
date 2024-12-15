# Bucle while
#  El cual requiere una condición para que se ejecute
#  Mientras suceda la condición, se ejecuta n veces

num = 0
while num <= 2: # si la condición se cumple, se ejecuta el ciclo
    print(f'Ejecutando el while {num} veces')
    num += 1

letra = ''
while letra != 'si':
    letra = input('Ingrese (si/No): ').lower()
else:
    print('Saludos!')

opcion = '0'
while opcion != '3':
    opcion = input("Ingresa una opción del 1 al 3: ")

print(f"Su opción elegida fue: {opcion}")