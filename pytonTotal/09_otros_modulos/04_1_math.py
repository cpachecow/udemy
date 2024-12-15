# El módulo math, contiene el kit completo para trabjar con números en Python.
# Desde trigonometría, matematica simple, tipo de redondeo, entre otros.

import math

# math.floor(): Hace un redondeo hacia abajo o hacia "el piso".
resultado = math.floor(89.665)
print(f'Redondeo hacia abajo de 89.665 : {resultado}')

# math.ceil(): Hace un redondeo hacia ariba o hacia "el techo".
resultado = math.ceil(89.665)
print(f'Redondeo hacia arriba de 89.665: {resultado}')

# math.pi: Es un valor de la constante PI.
resultado = math.pi
print(f'PI : {resultado}')

# math.log(): Calcula el logaritmo en donde recibe dos parámetros (resultado, base).
#             Significa a qué valor debe estár elevada 'base', para llegar a 'resultado'.
resultado = math.log(25, 5) # > 2
print(f'Log5(25): {resultado}')

# math.log10(): Calcula el logaritmo con base 10, recibe un parámetro (resultado).
#             Significa a qué valor debe estár elevada 'base =10', para llegar a 'resultado'.
resultado = math.log10(1000) # > 3
print(f'Log10(1000): {resultado}')

# math.sqrt(): Calcula la raíz cuadrada de un número.
resultado = math.sqrt(3)
print(f'Raíz cuadrada de \'3\' : {resultado}')

# math.sqrt(): Calcula la raíz cuadrada de un número.
resultado = math.factorial(7)
print(f'El factrial de \'7\' es : {resultado}')

# Trigonometría

# math.tan: Devuelve la tangente de un valor.
resultado = math.tan(180)
print(f'Tan(180) : {resultado}')

# math.cos: Devuelve el coseno de un valor.
resultado = math.cos(180)
print(f'Cos(180) : {resultado}')