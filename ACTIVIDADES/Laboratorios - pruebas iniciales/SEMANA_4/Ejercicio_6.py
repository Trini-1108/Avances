#Se tienen tres modelos de celulares, el modelo 1, 2, 3; el modelo 1 cuesta $60, 
# el modelo 2 cuesta $120, el modelo 3 cuesta $200,
# el programa debe ingresar la cantidad de celulares que se han vendido, 
# luego debe contar cuantos celulares de del modelo 1, 2, 3 se han vendido,
# también debe mostrar el total en dinero que se obtuvo de todas las ventas.

#Entrada:
print("="*50)
print(" => Bienvenido al programa de ventas de celulares")
print("="*50)

modelo1 = int(input(" => Ingrese la cantidad de celulares del modelo 1 vendidos= "))
modelo2 = int(input(" => Ingrese la cantidad de celulares del modelo 2 vendidos= "))
modelo3 = int(input(" => Ingrese la cantidad de celulares del modelo 3 vendidos= "))

#Proceso:
total_ventas = (modelo1*60) + (modelo2*120) + (modelo3*200)

#Salida:
print("="*50)
print(" => El total de ventas en dinero es= ", total_ventas)
print("="*50)
print(" => Elaborado por Trini")
print("="*50)
