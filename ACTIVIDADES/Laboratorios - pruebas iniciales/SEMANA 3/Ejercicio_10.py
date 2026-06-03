# Elaborar un programa que pida un número al usuario (del 1 al 7)
# escriba el nombre de ese día (por ejemplo, "martes" para el día 2). 
# Debes emplear el comando SEGUN.
#Entrada:
print("=" * 100)

numero= int(input("Ingrese un número del 1 hasta el 7: "))

#Proceso:
if numero == 1:
    print("El día es Lunes")
elif numero == 2:
    print("El día es martes")
elif numero == 3:
    print("El día es miércoles")
elif numero == 4:
    print("El día es jueves")
elif numero ==5:
    print("El dia es viernes")
elif numero == 6:
    print("El día es Sábado")
elif numero == 7:
    print("El día es Domingo")
else:
    print("Introduzca un número del 1 al 7, no otro número")

#Salida:
print("=" * 100)

print("El proyecto fue elaborado por: Trinidad Esteban")

print("=" * 100)