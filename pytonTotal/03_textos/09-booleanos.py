# Valores Booleanos, los que pueden tener un valor verdadero o falso.

# Asignacion directa
var1 = True
print(type(var1))
print(var1)

# Asignacion indirecta
num = 5 > 6 # Como no se cumple, se asigna un valor falso
print(type(num))
print(num)

num = bool(7>3)
print(type(num))
print(num)

lista = [1,2,3]
control = 4 in lista # Si encuentra el valor es 'True', de lo contrario es 'False'.
print(type(control))
print(control)