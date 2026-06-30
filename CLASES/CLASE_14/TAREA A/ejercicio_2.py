#ENTRADA:
def aña(simbolo ="=", longitud=50):
    print(simbolo*longitud)

def leer_datos():
    nombre_cliente = input("Ingrese el nombre del cliente: \n SU REPUESTA=> ")
    cantidad_de_productos = int(input("Ingrese la cantidad de productos: \n SU RESPUESTA=>  "))
    precio_unitario = float(input("Ingrese el precio unitario:\n SU REPUESTA=>  "))
    return nombre_cliente, cantidad_de_productos, precio_unitario

def calcular_el_total(cantidad, precio):
    return cantidad * precio

def mostrar_resultado(nombre, cantidad, precio, total):

    aña()
    print(f"Cliente: {nombre}")
    print(f"Cantidad de productos: {cantidad}")
    print(f"Precio unitario: {precio:.2f}")
    print(f"Importe total: {total:.2f}")
    aña()
    
#PROCESO y SALIDA:
aña()
nombre, cantidad, precio = leer_datos()
total = calcular_el_total(cantidad, precio)
mostrar_resultado(nombre, cantidad, precio, total)
