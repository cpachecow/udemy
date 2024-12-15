import numeros
from os import system

def pregunta():
    
    print("--- Bienvenido(a) al programa Generador de Turnos de Farmacia --- ")
    
    while True:
        

def inicio():

    bienvenida = """"""

    menu = """
            Selecciona las siguientes opciones:

             1.- [P] para Perfumería.
             2.- [F] para Farmacia.
             3.- [C] para Cosmética.

           """
    
    system('clear')
    print(bienvenida)

    while True:

        opcion = input(menu).upper()
        try:
            if opcion == 'P':
                system('clear')            
                print(next(numeros.gen_perfumes))

            elif opcion == 'F':
                system('clear')            
                print(next(numeros.gen_farmacia))

            elif opcion == 'C':
                system('clear')            
                print(next(numeros.gen_cosmetica))
        except:
            print("Favor seleccionar una opción correcta")
        

        try: 
            salir = input("Desea otra opción?: [S] o [N]: ").upper()
            ["S", "N"].index(salir)
        except ValueError:
                print("Esa no es una opción valida")
        else:
            if salir == "N":
                print("Gracias por la visita")
                break
                

inicio()
