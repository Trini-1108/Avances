#Pregunta 5: While 
# Escribe un programa que simule el juego de adivinar un número secreto. 
# El número secreto es el 12 (definido directamente en el código). El programa debe:
# 1.	Pedir al usuario que ingrese un número entre 1 y 20.
# 2.	Si el número ingresado es menor al secreto, mostrar: “El número secreto es mayor, intenta de nuevo”.
# 3.	Si el número ingresado es mayor al secreto, mostrar: “El número secreto es menor, intenta de nuevo”.
# 4.	Contar cuántos intentos lleva el usuario.
# 5.	Repetir hasta que el usuario adivine el número.
# 6.	Al adivinar mostrar: ¡Correcto! Adivinaste en X intentos.

#ENTRADA:
print("="*50)
print("BIENVENIDO AL JUEGO")
print("="*50)
secreto=12
numero=0
intentos=0
#PROCESO:
while numero != secreto:
    numero=int(input("INGRESE UN NUMERO DEL 1 AL 20: "))
    intentos+=1
    if numero<secreto:
        if numero < 0:
            print("Inválido")
        else:
            print("El numero secreto es mayor, ingrese de nuevo")
    elif numero>secreto:
        if numero > 20:
            print("Inválido")
        else:
            print("El numero secreto es menor, intente de nuevo")
else:
    print(f"¡CORRECTO!, lo adivinaste en {intentos} intentos")

#SALIDA:
print("="*50)
print("ELABORADO POR ESTEBAN TRINIDAD")
print("="*50)
