# if anidadas 
# Escribe un programa que simule el sistema de ingreso a un gimnasio. 
# El programa debe pedir el tipo de membresía (básica / premium), la edad y mostrar el acceso correspondiente según estas reglas:
# Si la membresía es premium:
#	Si tiene 18 años o más: Acceso completo: sala, piscina y clases.
#	Si es menor de 18: Acceso limitado, sala y clases únicamente.
# Si la membresía es básica:
#	Si tiene 18 años o más: Acceso a sala de máquinas únicamente
#	Si es menor de 18: Acceso denegado, menores solo con membresía premium
#  * Agregar un tercer requisito: si el cliente NO pago su membresia: acceso denegado, debe pagar su mensualidad.


#ENTRADA:
print("="*50)
print("BIENVENIDO AL PROGRAMA DE INGRESO A UN GIMNASIO!!")
print("="*50)

meb=input("INGRESE SU MEMEBRESIA (premium/ basico)= ").lower()
edad= int(input("INGRESE SU EDAD=> "))
pago= input("¿Pago su membresía? (Si/No)= ").lower()
import time
print("Espere...")
time.sleep(2)
#PROCESO:
print("="*50)           
if meb=="premium":
    if pago =="si":
        if edad>=18 and edad<=80:
            print("Acceso completo: sala, piscina y clases")
        else:
            print("Acceso limitado, sala y clases únicamente")
    else:
        print("ACCESO DENEGADO, DEBES PAGAR TU MEMBRESIA POBRE")
elif meb=="basico":
    if pago=="si":
        if edad >=18 and edad<=80:
            print("Acceso a sala de máquinas únicamente")
        else:
            print("Acceso denegado, menores solo con membresía premium")
    else:
        print("RECUERDA PAGAR TU MENSUALIDAD")
else:
    print("acceso denegado, la membresia no es válida")
print("="*50)
print("ELABORADO POR ESTEBAN TRINIDAD")
print("="*50) 