# ejemplos de algunos metodos más usados en textos

# upper: Transformar una cadena en mayusculas

texto = "Programacion en Python"
texto2 = texto.upper()
print(texto2)

# lower: Transformar una cadena en minusculas

texto3 = texto2.lower()
print(texto3)

# Split: separa una cadena de texto, quedado en una lista.

texto4 = texto.split() # si no hay nada, la cadena es separada por espacios
print(texto4)

texto5 = texto.split("en") # La cadena es separada por la palabra 'en'
print(texto5)

# Join: Une cadenas de texto, quedado en un string.

a = "Chile"
b = "es un país"
c = "muy bello"
union = " ".join([a,b,c]) #primer caracter es cómo se va a unir las cadenas
                          #  y el join hay que incluir las variables como lista.
print(union)

# find: Es muy similar a index(), pero si no encuentra un caracter arroja un -1

texto7  = texto.find("o")
print(texto7)

texto8  = texto.find("z")
print(texto8)

# replace: Reemplaza una parte de la cadena por otro texto

texto = "Esto es una prueba"
textor = texto.replace("prueba", "tarea")
print(textor)

# Los strings son inmutables, esto implica que no se pueden intercambiar por
# otros caracteres cuando ya tienen un valor.
texto9 = "Carlos" # no puedo cambiar la primera ni ningún catacter por la inmutabilidad de la variable.

# Se puede verificar si en un string hay una palabra
texto10 = "hola como te va, he estado escribiendo a tu correo y no he tenido respuesta"
print("correo" in texto10) # Busca la palabra 'correo' en el string, si lo cuentra es 'True' en caso contrario 'False'
print("refugio" in texto10)

# len: Longitud de un string
print(len(texto10))

