# Operaciones Bool, indican si son True o False
# Dependiendo si cumple con la condición.
# Pueden ser de cualquier tipo, string, int, etc.

mi_bool = 4 < 5 and 5 == (2 + 3)
print(mi_bool)

mi_bool = (10 == 1) or (9 == 9)
print(mi_bool)

texto = "Me gustan las montañas"

mi_bool2 = "gustan" in texto and "montañas" in texto
print("Verificando texto en una oración: ", mi_bool2)

mi_bool3 = not 'a' == 'a'
print(mi_bool3)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = (palabra1 not in frase) and (palabra2 not in frase)
print("Vericando si textos no están en un string: ", mi_bool)

