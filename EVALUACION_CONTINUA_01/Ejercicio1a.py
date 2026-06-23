# Pedir nota al Usuario:

# 1. Entrada:
nota=float(input("Ingrese su nota (0-20): "))

# 2. Proceso y Salida:
if 0<=nota<=10:
    print("Desaprobado")
elif 11<=nota<=14:
    print("Aprobado")
elif 15<=nota<=17:
    print("Bueno")
elif 18<=nota<=20:
    print("Excelente")
else:
    print("Nota inválida, ingrese una nota entre 0-20")
