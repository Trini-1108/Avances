# Membresía Gimnasio (incluyendo pago de mensualidad):

# 1.Entrada:
membresia=input("Ingrese tipo de membresía (basica/premium): ").lower()
edad=int(input("Ingrese su edad: "))
pago=input("¿pagó su membresía? (si/no): ").lower()

import time
print("Espere...")
time.sleep(3)

# 2. Proceso y Salida:
if pago=="no":
    print("Acceso denegado, debes pagar tu mensualidad")
else:
    if membresia=="premium":
        if edad>=18:
            print("Acceso completo: sala, piscina, etc.")
        else:
            print("Acceso limitado: sala y clases")
    elif membresia=="basica":
        if edad>=18:
            print("Acceso a sala de maquinas")
        else:
            print("Acceso denegado")
    else:
        print("Tipo de membresia no valido")
    