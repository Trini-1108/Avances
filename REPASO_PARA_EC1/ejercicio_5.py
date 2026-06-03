# Escribe un programa que pida una nota del 0 al 100 e imprima la calificación:

# 90–100 → "Excelente"
# 70–89 → "Bueno"
# 50–69 → "Regular"
# 0–49 → "Desaprobado"

#ENTRADA:
nota = int(input("INGRESE SU NOTA = "))

#PROCESO:
if nota >= 90 and nota <= 100:
    print("NOTA EXCELENTE")
elif nota >= 70 and nota <= 89:
    print("NOTA BUENA")
elif 50 <= nota <= 69:
    print("NOTA REGULAR")
elif 0 <= nota <= 49:
    print("NOTA DESAPROBADA")
else:
    print("NOTA INVALIDA; POR FAVOR INGRESE UNA NOTA DEL 0 AL 100")

print("ELABORADO POR ESTEBAN TRINIDAD")
