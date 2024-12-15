# Proyecto POO - Cuenta Bancaria

from os import system

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        # Con la clase super(), evitamos iniciar los atributos de la clase padre, en este caso Persona.
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir(self):
        datos_cliente = f"""
            ----------------------------------------------
              La información del cliente es :

               - Nombre: {self.nombre}
               - Apellido: {self.apellido}
               - Número de cuenta: {self.numero_cuenta}
               - Balance o saldo: {self.balance}
            ---------------------------------------------- 
                        """
        print(datos_cliente)

    def depositar(self, cantidad):
        self.balance = self.balance + cantidad
        print(f"Se ha depositado {cantidad} a su cuenta")
        return self.balance

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance = self.balance - cantidad
            print(f"Se ha retirado {cantidad} de su cuenta")
            return self.balance
        else:
            print("No se puede retirar una cantidad mayor al saldo actual")
            return False
        

def crear_cliente():
    nombre = input("Ingresar nombre cliente: ")
    apellido = input("Ingresar apellido del cliente: ")
    numero_cuenta = int(input("Ingresar numero de cuenta del cliente: "))
    balance = int(input("Ingresar el balance del cliente: "))
    
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    print("\nCliente creado satisfactoriamente")
    return cliente

def inicio():

    bienvenida = """
        --- Bienvenido(a) al programa Cuenta Bancaria ---

            - Favor ingresar algunos datos de cliente -

                """
    menu = """
            Selecciona las siguientes opciones:

             1.- Imprimir datos del cliente creado.
             2.- Generar depósito a tu cuenta.
             3.- Realizar un retiro de tu cuenta.

            *** Presione '4' para salir del programa ***

           """
    
    system('clear')
    print(bienvenida)
    cliente = crear_cliente()
    
    intento = 0
    while intento != 1:

        opcion = input(menu)

        if opcion == '1':
            system('clear')
            cliente.imprimir()

        elif opcion == '2':
            system('clear')
            cantidad = int(input("Indicar monto a depositar: "))
            cliente.depositar(cantidad)

        elif opcion == '3':
            system('clear')
            retiro = int(input("Indicar monto a retirar: "))
            cliente.retirar(retiro)
        
        elif opcion == '4':
            system('clear')
            print("\nHa salido satisfactoriamente\n")
            break

inicio()