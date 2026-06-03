#IMC : Peso/Altura**2

print("=-"*100)
peso= float(input("Por favor, ingrese su peso en kilogramos= "))
altura= float(input("Por favor, introduzca su altura en metros= "))

IMC = (peso)/(altura)**2

print(f"El resultado de tu IMC es:{IMC:.2f}")

print("="*100)
print("Tu IMC ES:",IMC)                                
if IMC>18.5:
 msg=("USTED TIENE BAJO PESO") 
elif 18.5 <= IMC >= 24.9:
 msg=("USTED ESTA EN PESO NORMAL")
elif 25 <= IMC >= 29.9:
 msg=("USTED ESTA CON SOBREPESO")
else:
 msg= ("USTED ESTA CON OBESIDAD")

print("=-"*100)

print ("Elaborado por Esteban Trinidad")