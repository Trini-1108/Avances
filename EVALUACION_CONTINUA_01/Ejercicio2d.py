# Membresía Gimnasio (utilizando AND):

# 1.Entrada:
membresia=input("Ingrese tipo de membresía (basica/premium): ").lower()
edad=int(input("Ingrese su edad: "))
pago=input("¿pagó su membresía? (si/no): ").lower()

import time
print("Espere...")
time.sleep(3)

# 2. Proceso y Salida:
if membresia=="premium" and pago=="si" and edad>=18:
    print("Acceso completo: sala, piscina y clases")
elif membresia=="premium" and pago=="si"and edad<18:
    print("Acceso limitado: sala y clases")
elif membresia=="premium" and pago=="no":
    print("Acceso denegado: debes pagar")
elif membresia=="basica" and pago=="si" and edad>=18:
    print("Acceso a sala de maquinas")
elif membresia=="basica" and pago=="si" and edad<18:
    print("Acceso denegado")
elif membresia=="basica" and pago=="no":
    print("Acceso denegado, debes pagar")
else:
    print("Tipo de membresia no valido")
    