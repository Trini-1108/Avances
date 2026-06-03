#Se requiere un algoritmo para determinar cuánto ahorrará una persona en un año.
#si al final de cada mes deposita variables cantidades de dinero.
#Se requiere saber cuánto lleva ahorrado cada mes.

#Entrada:
print("="*50)
print("Bienvenido al programa de ahorro anual")
print("="*50)

ahorro_total = 0
#Proceso:
for mes in range(1, 12 + 1):
    ahorro_mes = float(input(f"Ingrese el monto ahorrado durante el mes {mes}= "))
    ahorro_total += ahorro_mes
    print(f"Total ahorrado al final del mes {mes}: {ahorro_total:.2f}")

#Salida:
print(f"Total ahorrado al final del año: {ahorro_total:.2f}")

print("="*50)
print("Este trabajo fue realizado por: Trini")
print("="*50)
