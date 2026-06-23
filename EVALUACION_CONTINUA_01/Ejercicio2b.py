# Membresía Gimnasio (incluyendo pago de mensualidad):

# 1.Entrada:
membresia=input("Ingrese tipo de membresía (basica/premium): ").lower()
edad=int(input("Ingrese su edad: "))
pago=input("¿pagó su membresía? (si/no): ").lower()

# 2. Proceso y Salida:
if membresia=="premium":
    if pago=="si":
        if edad>=18:
            print("Acceso completo: sala, piscina, etc.")
        else:
            print("Acceso limitado: sala y clases")
    else:
        print("Acceso denegado: debes pagar tu membresía")
elif membresia=="basica":
    if pago=="si":
        if edad>=18:
            print("Acceso a sala de maquinas")
        else:
            print("Acceso denegado")
    else:
        print("Acceso denegado: debes pagar tu mensualidad")
else:
    print("Tipo de membresia no valido")
    