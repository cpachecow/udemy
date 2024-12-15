from datetime import datetime

# datetime(): Se puede agregar la fecha y la hora segun el ejemplo a continuación
#             También se puede rescatar la información de hora, año, minuto, etc.
mi_fecha = datetime(2024,10,4,15,45,59)
print(mi_fecha)
print(mi_fecha.year)
print(mi_fecha.hour)

# replace(): Sirve para modificar un argumento de datetime.
mi_fecha = mi_fecha.replace(month=11)
print(mi_fecha)

# datetime.now(): indicará la fecha y hora actual
print(f'Fecha y hora actual: {datetime.now()}')

# datetime.now(),time(): indicará horario actual
print(f'Horario actual: {datetime.now().time()}')