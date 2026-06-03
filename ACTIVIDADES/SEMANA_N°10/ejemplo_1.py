# Crear una aplicación en Python en el cual en un almacén se hace un descuento de 20%
# a los clientes cuya compra supere los S/. 1000, imprimir cuál será la cantidad que pagará
# una persona por su compra.

#Entrada:
print("="*80)
print("=== BIENVENIDO AL PROGRAMA DE MOTOS ===")
print("="*80)
monto= int(input("INGRESE EL MONTO: \n Su repuesta=>  "))
#Proceso:
print("="*80)
if monto >=1000:
    print("Usted por superar los S/. 1000, tiene un descuento")
    desc= monto * 0.20
    monto_final= monto - desc
    print(f"Descuento: S/. {desc:.2f}")
    print(f"Total de pagar: S/. {monto_final:.2f}")
else:
    print(f"Total a pagar: \n S/. {monto:.2f}")
print("="*80)

