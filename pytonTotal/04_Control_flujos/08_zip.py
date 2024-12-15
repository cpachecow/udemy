# El objeto zip combina dos o más listas que tengan el mismo largo
# en caso de tener tamaños distintos, iguala valores con la lista que tiene menos datos.
# Estas se guardan en tuplas.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for c, p in list(zip(capitales,paises)):
    print(f'La capital de {p} es {c}')
print('\n')

marcas = ['Garmin', 'La Sportiva', 'Silva', 'Julbo']
productos =['GPS', 'Zapato de montaña', 'Brújula', 'Lente de sol']
mi_zip = list(zip(marcas, productos))
print(mi_zip)
print('\n')

trad = ['uno / um / one','dos / dois / two', 'tres / três / three', 'cuatro / quatro / four', 'cinco / cinco / five']
num = [1,2,3,4,5]
for i, valor in list(zip(num, trad)):
    print(f'{i}: {valor}')
print('\n')

