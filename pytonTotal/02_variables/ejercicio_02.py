
vendedor = input("Estimado trabajor, favor dame tu nombre: ")
venta = input("Favor indicar valor total de tus ventas: $ ")
venta = int(venta)

comision = venta * 0.13
comision = round(comision, 5)

print(f"Estimado(a) {vendedor} tu comisión es de $ {comision}")

print('Que estés muy bien!')