# Escribe un programa que siga pidiendo números al usuario hasta que ingrese el número 0, 
# y al final imprima cuántos números ingresó.

#ENTRADA:
intentos = 0
while True:
    numero = int(input("INGRESE UN NÚMERO ==  "))
    intentos= intentos + 1
    if numero==0:
        break

print(f"usted ingresó un total de {intentos-1} números").lower()

print("ELABORADO POR ESTEBAN TRINIDAD")

