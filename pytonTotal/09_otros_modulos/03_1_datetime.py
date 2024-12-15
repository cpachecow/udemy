import datetime

# Contiene un sinfin de métodos para fecha y hora

# time(): se puede definir hora, minutos, segundos y después 
#         puede rescartar dichos valores.
mi_hora = datetime.time(17,35,18)
print(f'- Hora configurada: {mi_hora}')
print(mi_hora.hour)
print(mi_hora.minute)
if(mi_hora.hour >= 17 and mi_hora.minute > 35):
    print('El horario cumple con las condiciones')
else:
    print('El horario no cumple con las condiciones')
    
# date(): se puede definir año, mes, día y después 
#         puede rescartar dichos valores.
mi_dia = datetime.date(1985,11,5)
print(f'\n- Fecha indicada: {mi_dia}')
print(mi_dia.year)
print(mi_dia.month)
print(mi_dia.day)

# today(): puedo rescatar el día actual
hoy = datetime.date.today()
print(f'Fecha actual: {hoy}')