# Comprensión de Listas: Es una forma de crear una lista de manera más eficiente

# La forma convencional
lista = []
palabra = 'Hola Mundo'

for letra in palabra:
    lista.append(letra)
print(lista)

# Comprensión Lista:
palabra2 = 'El rock me encanta'
lista2 = [letra2 for letra2 in palabra2]
print(lista2)

lista2 = [letra2 for letra2 in 'Donde está Joe Black?']
print(lista2)

lista3 = [n/2 for n in range(1,5)]
print(lista3)

lista4 = [n for n in range(0,10) if(n > 5)]
print(lista4)

lista5 = [n if(n > 2) else 'no' for n in range(0,10)]
print(lista5)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrados = [n**2 for n in valores]
print(valores_cuadrados)

# Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if(n%2==0)]
print(valores_pares)

# Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores
# en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo
# de unidades es la siguiente: °C = (°F - 32) * (5/9)
temperatura_fahrenheit = [32, 212, 275]
grados_celcius = [(n-32)*(5/9) for n in temperatura_fahrenheit]
print(grados_celcius)