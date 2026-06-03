#IMC : Peso/Altura**2
#Utilizando and
#Entrada:
print("=-"*100)
peso= float(input("Por favor, ingrese su peso en kilogramos= "))
altura= float(input("Por favor, introduzca su altura en metros= "))

#Proceso:
IMC = (peso)/(altura**2)

#salida:
print("=-"*100)

print(f"El resultado de tu IMC es:{IMC:.2f}")
if IMC<=18.5:
    print("USTED TIENE BAJO PESO") 
elif IMC<18.5 and IMC<=24.9:
    print("USTED ESTA EN PESO NORMAL")
elif IMC<25 and IMC<=29.9:
    print("USTED ESTA CON SOBREPESO")
else:
    print("USTED ESTA CON OBESIDAD")

print("=-"*100)

print ("Elaborado por Esteban Trinidad")

print("==" *100)