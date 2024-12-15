#  *** Ejercicio día 3 ***
#  Debe ingresar un texto cualquiera y adicionalmente tres letras, para luego procesar:
#  1.- Indicar cuántas veces se encuentran las letras seleccionadas, en el texto ingresado.
#  2.- Cuántas palabras hay en todo el texto.
#  3.- Cuál es la primera letra y la última del texto.
#  4.- Invertir el órden de las palabras del texto.
#  5.- Verificar si la palabra 'Python se encuentra dentro del texto'

texto = input("Favor ingresar un texto: ")
a = input("Favor ingresar una letra cualquiera: ")
b = input("Favor ingresar una letra cualquiera: ")
c = input("Favor ingresar una letra cualquiera: ")

a = a.lower()
b = b.lower()
c = c.lower()
texto3 = texto.lower()

texto2 = list(texto)


print(f"1.- La letra '{a}' se encuetra {texto3.count(a)} veces en el texto")
print(f"1.- La letra '{b}' se encuetra {texto3.count(b)} veces en el texto")
print(f"1.- La letra '{c}' se encuetra {texto3.count(c)} veces en el texto")

palabras =  texto.split()
print("2.- La cantidad de palabras en el texto ingresado es: ", len(palabras))

print("3.- La primera letra del texto es: ", texto[0])
print("3.- La última letra del texto es: ", texto[len(texto2)-1])

print("4.- El texto en reverso: ", texto[-1])

verif = 'Python'
verif2 = verif.lower() in texto.lower()
if verif2 == True:
    print("5.- La palabra 'Python' está en el texto")
else:
    print("5.- La palabra 'Python' no está en el texto")


