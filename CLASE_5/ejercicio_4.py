# Ingrese 5 montos de ventas y cuantas son mayores a S/.1000:

print("="*50)
print("Ingreso de ventas")
print("="*50)

total_ventas=0
ventas_mayores_1000=0

for a in range (1,5):
    venta=float(input(f"Ingrese el monto de la venta {a}: S/. "))
    total_ventas+=venta

    if venta >1000:
        ventas_mayores_1000+=1

print("="*50)
print("Total vendido: S/. ", total_ventas)
print("ventas mayores a S/.1000: " , ventas_mayores_1000)
print("="*50)

