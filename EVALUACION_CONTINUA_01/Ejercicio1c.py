# Pedir nota al Usuario:

# 1. Entrada:
nota=float(input("Ingrese su nota (0-20): "))

# 2. Proceso y Salida:
if 0<=nota<=10:
    print("Desaprobado")
elif nota<=14:
    print("Aprobado")
elif nota<=17:
    print("Bueno")
elif nota<=20:
    print("Excelente")
else:
    print("Nota inválida, ingrese una nota entre 0-20")
