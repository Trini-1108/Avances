# Realice un algoritmo que permita determine el monto de bono que recibirá un profesor 
# (debe capturar el valor del salario mínimo y los puntos del profesor).
# El bono se determina de la siguiente manera:
#Puntos:
#0-100
#101-150
#151 - en adelante
#Premio:
#1 salario mínimo
#2 salarios mínimos
#3 salarios mínimos


#Entrada:
print("="*50)
salario_minimo = float(input("Ingrese el valor del salario mínimo: "))
puntos = int(input("Ingrese los puntos del profesor: "))

#Proceso:
if puntos >= 0 and puntos <= 100:
    bono = salario_minimo * 1
elif puntos >= 101 and puntos <= 150:
    bono = salario_minimo * 2
elif puntos >= 151:
    bono = salario_minimo * 3
else:
    bono = 0
    print("Los puntos no pueden ser negativos")

#Salida:
print("=" * 50)
print(f"El bono que rebicirá el profesor es: {bono}")
print("=" * 50)
print("El proyecto fue elaborado por: Trinidad Esteban")
print("=" * 50)