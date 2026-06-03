# Inversión en el Banco:

# 1. Entrada:
capital=float(input("Ingrese el monto a invertir S/.: "))
tasa=float(input("Ingrese tasa anual %: "))

# 2. Proceso:
interes=capital*(tasa/100)

# 3. Salida:
print("Reporte de Inversión")
print("Capital invertido S/.: ", capital)
print("tasa de interés: %", tasa)
print("Intereses ganados: ", interes)

if interes>7000:
    total=capital+interes
    print("Los intereses exceden los S/. 7,000 soles")
    print("Se recomienda reinvertir")
    print("Dinero total en cuenta: ", total)
else:
    print("No se recomienda reinvertir")
    print("Interés a retirar: ", interes)

    


