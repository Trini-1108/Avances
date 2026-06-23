# Pedir nota al Usuario(usando AND):

# 1. Entrada:
nota=float(input("Ingrese su nota (0-20): "))

# 2. Proceso y Salida:
if nota>=0 and nota<=10:
    print("Desaprobado")
elif nota>=11 and nota<=14:
    print("Aprobado")
elif nota>=15 and nota<=17:
    print("Bueno")
elif nota>=18 and nota<=20:
    print("Excelente")
else:
    print("Nota inválida, ingrese una nota entre 0-20")
