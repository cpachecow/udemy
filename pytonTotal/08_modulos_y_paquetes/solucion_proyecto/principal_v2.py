import numeros

def preguntar():

    print("\nBienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_rubro)

def inicio():

    while True:
        preguntar()
        try:
            
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            # ["S", "N"].index(otro_turno)
            if otro_turno not in ('S', 'N'):
                raise ValueError
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("\nGracias por su visita\n")
                break

inicio()
