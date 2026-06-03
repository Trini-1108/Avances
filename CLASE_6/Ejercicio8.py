
# Trabajando Tipo de Cambio con Diccionarios:

# Tipo de Cambio:

#          clave  valor
dcambios={"euro":4.5, "dolar":3.2, "yen":7.1}

# Ingresamos valores:

soles=float(input("Ingrese cantidad en soles: "))
moneda=input("Introduce la moneda de cambio [euro, dolar, yen]: ")

print(soles)
print(moneda)

cambio=soles/(dcambios.get(moneda))

print(cambio)

