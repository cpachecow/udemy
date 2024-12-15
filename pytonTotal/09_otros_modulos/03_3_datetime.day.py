from datetime import date

# date(): me permite realizar operaciones matemáticas con las fechas

nacimiento = date(1982,12,8)
hoy = date.today()
edad = (hoy - nacimiento)
edad = edad.days/365
edad = int(round(edad, 3))
print(f'La persona tiene {edad} años')