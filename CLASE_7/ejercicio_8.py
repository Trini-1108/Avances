#Ejercicio de Banco:

print("="*50)
print("BIENVENIDO AL BANCO DE PRESTAMOS!!!!")
print("="*50)

sueldo= int(input("INGRESE SU SUELDO MENSUAL ==>  "))
if sueldo <1500:
        print("Usted tiene 6 puntos")
elif 1500>= sueldo <= 6000:
        print("Usted tiene 12 puntos")
else:
        print("Usted tiene 18 puntos")

vivienda= input("SELECCIONE LA VIVIENDA DONDE ESTAS (parientes/alquilada/propia)==>  ").lower()
if vivienda == "parientes":
        print("Usted tiene 2 puntos")
elif vivienda == "alquilada":
        print("Usted tiene 5 puntos")
else:
        print("Usted tiene 10 puntos")

tarjeta= input("¿Posees alguna tarjeta de crédito?. (S/N)  ==>  ").lower()
if tarjeta == "S":
    print("Usted tiene 6 puntos")
else:
    print("Usted tiene 0 puntos")
familia= input("¿Posees una carga familiar?. (S/N) ==>  ")
if tarjeta == "S":
        print("Usted tiene 6 puntos")
else:
        print("Usted tiene 3 puntos")

print("="*50)
total= "sueldo" + "vivienda" + "tarjeta" + "familia"

print("Usted tiene {} puntos", total)

if total >=20:
    print("USTED TIENE EL PRESTAMO")
else:
    print("USTED NO PUEDE TENER EL PRESTAMO")

print("="*50)
print("ELABORADO POR ESTEBAN TRINIDAD")
print("="*50)
