# Adivinar el número secreto:

# 1. Entrada:
secreto=12
numero=0
intentos=0

# 2.Proceso y Salida:
while numero!=secreto:
    numero=int(input("Ingrese un número entre 1 y 20: "))
    intentos+=1

    if 1<= numero <=20: # Sólo procesa en ese rango
        if numero<secreto:        
            print("El número secreto es mayor, intenta nuevamente")
        elif numero>secreto:
            print("El numero secreto es menor, intentar nuevamente")
    else:
        print("Numero fuera de rango")
else:
    print(f"Correcto!!! Adivinaste en {intentos} intentos")
