# ...existing code...
print("="*50)
print("Ingreso de ventas")
print("="*50)

total_ventas = 0.0
ventas_mayores_1000 = 0

# Cambio: iterar 5 veces (1..5) y validar entrada
for a in range(1, 6):
    while True:
        try:
            venta = float(input(f"Ingrese el monto de la venta {a}: S/. "))
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    total_ventas += venta
    if venta > 1000:
        ventas_mayores_1000 += 1

print("="*50)
print(f"Total vendido: S/. {total_ventas:.2f}")
print(f"Ventas mayores a S/.1000: {ventas_mayores_1000}")
print("="*50)
