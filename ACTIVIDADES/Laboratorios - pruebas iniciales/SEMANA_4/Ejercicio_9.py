#Calcular el precio total de una compra de “n” productos (el valor de “n” se ingresa por teclado). 
# Se ingresa el precio de cada producto y la cantidad de "n" productos comprada de este. 
# Emplear la estructura while.

#Entrada:
print("="*50)
print("Bienvenido al programa de calculo de precio total")
print("="*50)
#Proceso:
i= 1
n = int(input("Ingrese la cantidad del producto {}: ".format(i)))
precio= float(input("Ingrese el precio del producto {}: ".format(i)))
total = 0
while i <= n:
    total += precio * n
    i += 1
#Salida:
print("El precio total es: ", total)
print("=" *50)
print("Elaborado por Trini")
print("=" *50)
