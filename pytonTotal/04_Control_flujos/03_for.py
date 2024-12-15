# Uso del ciclo for

# Ejemplo 01
nombres = ['Raul', 'Carlos', 'Ana', 'Juan','Angela']
for i in nombres:
    print(i)
print('\n')
# la variable i es interna al ciclo for, dado que representará todo el contenido de la lista nombre.

# Ejemplo 02
letras = ['a', 'b', 'c', 'd']
x = 0
for l in letras:
    print(f'Letra[{x}]: {l}')
    x += 1
print('\n')
# Ejemplo 03 -> Uso index(): el cual indica la posición de cada contenido

cuerpo = ['ojos', 'dientes', 'corazón', 'piernas']
for c in cuerpo:
    print(f'Partes del cuerpo {cuerpo.index(c)}: {c}')

# Ejemplo 04 -> startwith busca un si un texto se inicia con una letra específica.
nombres2 = ['Raul', 'Carlos', 'Ana', 'Juan','Angela', 'Alberto', 'Andrea', 'Cristian', 'Claudia']
letra_ini = 'C'
print(f'\nSe imprimiran los nombres que comiencen con la letra {letra_ini}:')
for n in nombres2:
    if n.startswith(letra_ini):
        print(n)
print('\n')

# Ejemplo 05 -> recorrer varias listas
print('Recorriendo listas con listas en su contenido')
objeto = [[1,2], [3,4], [5,6]]
for z in objeto:
    print(z)
for a,b in objeto:
    print(a)
    print(b)
print('\n')

# Ejemplo 06 -> Recorrer diccionarios

print('Recorriendo diccionarios')
dicc = {'clave1':1, 'clave2': 2, 'clave3':3}
for d in dicc:
    print(d)
for d in dicc.values():
    print(d)
for d in dicc.items():
    print(d)
for a,b in dicc.items():
    print(a,b)