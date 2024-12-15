import time
# Este modulo nos podría servir para medir el tiempo cuánto tarda una función 
# con respecto a otra. Simplemente se calcula el tiempo inicial, posterior a la
# ejecución de la función, tiempo final y realizo una resta para saber cuánto
# fueron los segundos totales de ejecución.

# El pero de este módulo es que para ejecuciones pequeñas, no se logra ver la
# diferencia de tiempos de ejecución. Por lo tanto, hay que configurar dichas
# funciones para que corran por un timepo mayor para que sean medibles.
# Si la constante NUMERO = 100, la diferencia de tiempo sería casi cero.

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero :
        lista.append(contador)
        contador+=1
    return lista

NUMERO = 1_000_000

inicio = time.time()
prueba_for(NUMERO)
fin = time.time()
tiempo_total1 = fin - inicio
print(f'Tiempo for: {tiempo_total1}')

inicio = time.time()
prueba_while(NUMERO)
fin = time.time()
tiempo_total2 = fin - inicio
print(f'Tiempo while: {tiempo_total2}')
print((1-(tiempo_total1/tiempo_total2))*100)