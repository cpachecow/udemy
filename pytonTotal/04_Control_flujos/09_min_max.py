# funciones Min y Max

lista = [1,3,6,8,9,10,14,3,23]
print(min(lista))
print(max(lista))
print('\n')

# En un diccionario encontrar el valor mínimo y el último nombre ordenado de forma alfabética.
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(f'Valores del diccionario: edad mínima: \'{edad_minima}\', y el último normbre: \'{ultimo_nombre}\'')
