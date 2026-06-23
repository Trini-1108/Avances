# Pregunta 3: if · elif · else (5 pts.)

# Escribe un programa en Python que pida al usuario ingresar su nota final (un número entre 0 y 20) 
# Muestre el siguiente mensaje según el resultado:

# De 0 a 10: Desaprobado
# De 11 a 14: Aprobado
# De 15 a 17: Bueno
# De 18 a 20: Excelente
 

#ENTRADA:
print("="*50)
print("BIENVENIDO AL PROGRAMA DE NOTA FINAL")
print("="*50)
a=int(input("ingrese un númmeo del 1 al 20=" ))

#PROCESO Y SALIDA:
print("="*50)

if a>=0 and a<= 10:
    print("USTED ESTA DESAPROBADO")
elif a>=11 and a<=14:
    print("USTED ESTA APROBADO")
elif a>=15 and a<=17:
    print("USTED TIENE UNA NOTA BUENA")
elif a>=18 and a<=20:
    print("USTED ESTA CON UNA NOTA DE EXCELENCIA, FELICIDADES!!!")
else:
    print("INGRESE UNA NOTA DEL 1 AL 20")

print("="*50)
print("EL PROGRAMA FUE ELABORADO POR ESTEBAN TRINIDAD")
print("="*50)