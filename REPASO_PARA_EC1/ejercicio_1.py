# uso de if, elif y else
# Cálculo del Índice de Masa Corporal
# Solicite que al usuario ingrese su peso en kilogramos, su altura en metros.
# IMC = peso / (altura)**2
# El IMC tiene que ser con dos decimales.
# Clasifiquelo de la siguiente manera:
# Bajo peso: IMC < 18.5
# Normal: 18.5 <= IMC < 24.9
# Sobrepeso: 25 <= IMC < 29.9
# Obesidad: IMC >= 30

# ENTRADA:
print("="*50)
peso = float(input("Ingrese su peso en kilogramos (Kg): "))
altura= float(input("Ingrese su altura en metros (m): "))

#Proceso:
print("="*50)
IMC = peso / (altura)**2

#Salida:
print(f"Su IMC es: {IMC:.2f}")
if IMC < 18.5:
    print("Usted tiene bajo peso")
elif 18.5 <= IMC < 24.9:
    print("Usted tiene un peso normal")
elif 25 <= IMC < 29.9:
    print("Usted tiene sobrepeso")
else:
    print("Usted tiene obesidad")

print("="*50)
print("El programa fue elaborado por Trini")
print("="*50)

