# Ingresar 5 notas y contar cuantos aprobados y desprobados.

#Entrada:

print("="*50)

m=0
aprobados=0
desaprobados=0

#Proceso:
while m<=4:
    nota=int(input("Ingrese la nota que desea del 1 al 20: "))

    if nota>=12:
        aprobados+=1
    else:
        desaprobados+=1
        m=m+1
    
#Salida:
print("="*50)
print("Numero de aprobados:", aprobados)
print("Numeros de desaprobados: ",desaprobados)
print("="*50)
print("Este trabajo fue elaborado por Trinidad Esteban")

