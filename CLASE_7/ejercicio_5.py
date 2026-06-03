print("="*50)

#Trabajando un tipo de cambio con el diccionario:

#tipo de cambio:
#           clase valor
dcambios= {"euro":4.5, "dolar":3.2, "yen":7.1}

#Ingresando valores:
soles= float(input("Ingrese cantidad de soles: "))
moneda= input("INTRODUZCA LA MONEDA DE CAMBIO [euro, dolar, yen]:  ")
print(soles)
print(moneda)

cambio =soles/ (dcambios.get(moneda))
print(cambio)

