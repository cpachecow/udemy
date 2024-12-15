# Programa debará eligir una palabra al azar y mostrarla en guiones. 
# A medida que vayamos adivinando las palabras, estas se tiene que desplegar. Con un máximo de 6 vidas.

from random import choice
import re

VIDAS = 6
PALABRAS = ['hola', 'Mundo', 'Bindy','Lobo','Freya','Metallica','Paradoja','Guitarra','Playa','relax']

def palabraAzar(palabra):
    palabra_aleatoria = choice(palabra)

    if palabra_aleatoria:
        return palabra_aleatoria.lower()
    else:
        return None

def mostrarGuiones(texto):
    if texto:
        guion = len(texto) * "-"
        return guion
    else:
        return None  

def jugarAhoracado(VIDAS):

    texto = palabraAzar(PALABRAS)
    # print(texto)
    texto2 = list(texto)

    texto3 = []
    texto3 = list(mostrarGuiones(texto))
    letras_incorrectas = []
    letras_correctas = []

    titulo = '''\n*** Hola, bienvenido(a) al juego del Ahorcado ***\nAtrévete a adivinar la siguiente palabra:\n'''
    print(titulo, texto3)

    while VIDAS > 0:

        letra = input("\nIngresa una letra para adivinar la palabra: ")
        es_letra = re.findall("[a-zA-Z]", letra)

        if es_letra:

            if(letra in letras_correctas):
                VIDAS-=1
                print(f'La letra \'{letra}\' ya se , le quedan {VIDAS} intentos.')
                print(texto3)
                print('\n')
                continue
            else:
                if letra in texto2:
                    
                    letras_correctas.append(letra)
                    
                    for count, value in enumerate(texto2):
                        if(letra == value):
                            texto3[count] = value

                    print(f'Excelente se encontró la letra: \'{letra}\', le quedan {VIDAS} intentos')
                    print(texto3)
                    print('\n')
                    
                    if texto3 == texto2:
                        print("\n\n*** Ganaste, Felicidades!!!! ****\n\n")
                        break
                else:
                    VIDAS-=1

                    if letra not in letras_incorrectas:
                        letras_incorrectas.append(letra)
                    
                    print(f'No se encontró la letra \'{letra}\', le quedan {VIDAS} intentos.')
                    print(f'Letras incorrectas: {letras_incorrectas}.')
                    print(texto3)
                    print('\n')
        else:
            VIDAS-=1
            print("\nDebe escribir una sola letra, desde la 'a' hasta la 'z'\n")
            print(f'Le quedan {VIDAS} intentos.\n')
            print(texto3)
            print('\n')
    else:
        print('Lo siento haz perdido xP\n')

jugarAhoracado(VIDAS)


