# Realizar un algoritmo que permita calcular las operaciones básicas. 
# Ingresando 2 valores cualquiera. Se debe pedir que operación se va a realizar (+, -, x, ÷). Usar el comando SEGÚN
# Creo que tengo que poner una aclaración, SEGUN = if, else, elif.
print("="*100)

#1. Entrada:
a = int(input("Ingrese primer numero: "))  
b = int(input("Ingrese segundo numero: "))
operacion = input("Ingrese la operación a realizar [+, -, x, ÷]: ")

#2. Proceso:
if operacion == "+":
    resultado = a + b
elif operacion == "-":
    resultado = a - b
elif operacion == "x" or "*":
    resultado = a * b
elif operacion == "÷":
    resultado = a / b
else:
    resultado = "La operación no se puede realizar"

#3. Salida:
print("El resultado de la operación es: ", resultado)

print("="*100)

print("el trabajo fue realizado por: Trinidad Esteban")

print("="*100)
