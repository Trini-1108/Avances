# La tienda “El buen vecino”. Desea calcular el monto a pagar de sus clientes. 
# Dependiendo del producto a elegir. (menestras, cereales, lácteos). 
# Para ello se debe ingresar la cantidad y precio del producto. 
# Usar el comando SEGÚN. 

#Entrada:
print("="*100)
el_buen_vecino = input("Ingrese el producto que deseas calcular (menestras, cereales y lacteos)): ")
cantidad = int(input("Ingrese usted la cantidad del producto que ordeno: "))
precio = float(input("Ingrese el precio del producto: "))
#Proceso:
if el_buen_vecino == "menestras":
    monto_total1 = cantidad * precio
    print("El monto total de pagar las menestras es: ", monto_total1)
elif el_buen_vecino == "cereales":
    monto_total2 = precio * cantidad
    print("El monto total de pagar los cereales es: ", monto_total2)
elif el_buen_vecino == "lacteos":
    monto_total3= precio * cantidad
    print("El monto total de pagar los lacteos es de: ", monto_total3)
else:
    print("El producto que usted selecciono no se encuentra en el sistema")
#Salida:
print("="*100)
print("El proyecto fue elaborado por: Trinidad Esteban")
print("="*100)
