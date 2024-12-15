# La función enumerate( ) nos facilita llevar la cuenta de las
# iteraciones, a través de un contador de índices de un iterable,
# que se puede utilizar de manera directa en un loop, o
# convertirse en una lista de tuplas con el método list( ).

print(list(enumerate("Hola")))
print('\n')

lista = ['a','b','c','d','e']
for i, valor in enumerate(lista):
    print(i, valor)
print('\n')

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
print('\n')

# Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i, valor in enumerate(lista_nombres):
    if valor.startswith('M'):
        print(i, valor)