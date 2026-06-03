# Uso de if, elif y else.
# Solicite al usuario la temperatura en grados celsius.
# Muestre la temperatura ingresada con 1 decimal.
# Temperatura < 0 : Bajo cero, en alerta helada.
# 0.1<= temperatura <= 9.9 : Muy frío, abrigate bien.
# 10 <= temperatura <= 19.9 : Frío, lleva abrigo.
# 20 <= temperatura <= 29.9 : Templado, clima agadable.
# 30 <= temperatura <= 39.9 : Caluroso, hidrátate.
# temperatura => 40 : Entremo, alerta de calor.

#ENTRADA:
print("="*50)
print("Bienvenido a la recopilación de temperantura")
print("="*50)

temp = float(input("Ingrese en grados celsius la temperatura actual: "))

#PROCESO:
print("="*50)
print(f"Temperatura: {temp:.1f} °C")

#SALIDA:
print("="*50)
if temp < 0:
    print("Clasificación: Bajo cero")
    print("Alerta: Helada")
elif temp < 10:
    print("Clasificación: Muy frío")
    print("Alerta: Helada")
elif temp < 20:
    print("Clasificación: Frío")
    print("Alerta: Abrigate bien")
elif temp < 30:
    print("Clasificación: Templado")
    print("Alerta: Clima agadable")
elif temp <40:
    print("Clasificación: Caluroso")
    print("Alerta: Hidrátate")
else:
    print("Clasificación: Extremo")
    print("Alerta: Alerta de calor")

print("="*50)
print("Elaborado por Trini")
print("="*50)
