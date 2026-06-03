#1. Entrada:
print("="*50)
capital= float(input("Ingrese el monto de la capital ==>  "))
tasa=float(input("Ingrese la tasa en decimales ==>  "))
print("="*50)

#2. proceso:
interes= capital*(tasa/1000)

#3. salida: 
print("Reporte de Inversión ==>  ")
print("Capital invertido S/.: ", capital)
print("Tasa de interés: %", tasa)
print("Intereses ganados:  ", interes)

print("="*50)

if interes > 7000:
    print("SE RECOMIENDA INVERTIR")
    print("LOS INTERESES EXCEDE A LOS S/. 7000")
else:
    print("NO SE RECOMIENDA REINVERTIR")

print("="*50)
print("ELABORADO POR ESTEBAN TRINIDAD")
print("="*50)
