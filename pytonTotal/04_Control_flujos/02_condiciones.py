# Condiciones if elif y else

num1 = 10
num2 = 20

if num1 > num2:
    print("Correcto")
else:
    print("incorrecto")

edad = 16
nota = 2

if edad > 18:
    print("Eres mayor de edad")
    if nota > 3.99:
        print("Haz pasado tu curso")
    else:
        print("Haz reprobado")
else:
    print("Eres menor de edad")
    if nota > 3.99:
        print("Haz pasado tu curso")
    else:
        print("Haz reprobado")


num01 = input("Ingresa un número: ")
num02 = input("Ingresa otro número: ")


if num01 > num02:
    print(f"{num01} es mayor que {num02}")
elif num02 > num01:
    print(f"{num02} es mayor que {num01}")
else:
    print("Los números ingresados son iguales")
