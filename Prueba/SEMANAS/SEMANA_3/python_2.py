# calculo de riesgo cardiovascular:
#Entrada <3
print("=-"*100)
edad=int(input("Ingrese su edad: "))
peso= float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura:"))

#Proceso:
imc = (peso)/(altura**2)

#salida:
print(f"Su IMC es:{imc:.2f}")

if edad>=40:
    if imc>=25:
        print("Riesgo Alto, mayor de 40 años con sobrepeso")
    else:
        print("Riesgo Medio, mayor de 40 años con peso normal")
else:
    if imc>=25:
        print("Riesgo Medio, joven con sobrepeso")
    else:
        print("Riesgo Bajo, persona joven con peso normal")

print("=-"*100)

print("Elaborado por Trini")

print("=-"*100)