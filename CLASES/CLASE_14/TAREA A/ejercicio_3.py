#ENTRADA:
def awa(simbolo="=", longitud=50):
    print(simbolo*longitud)

def leer_prestamos():
    awa()
    cantidad = int(input("Ingrese la cantidad de préstamos a registrar: \n SU REPUESTA=> "))
    awa()

    nombres = []
    cantidades = []
    
    for a in range(cantidad):
        nombre = input(f"Nombre del lector #{a+1}:\n SU REPUESTA=>  ")       
        libros = int(input(f"Cantidad de libros prestados a {nombre}: \n SU REPUESTA=>  "))
        while libros < 1 or libros > 5:
            print("Error: la cantidad debe estar entre 1 y 5.")
            libros = int(input(f"Cantidad de libros prestados a {nombre}: \n  "))
        nombres.append(nombre)
        cantidades.append(libros)
    return nombres, cantidades

def calcular_total(cantidades):
    return sum(cantidades)


def calcular_promedio(cantidades):
    return calcular_total(cantidades) / len(cantidades)


def buscar_maximo(cantidades):
    return max(cantidades)


def buscar_minimo(cantidades):
    return min(cantidades)


def mostrar_resultados(nombres, cantidades):

#PROCESO:

    total = calcular_total(cantidades)
    promedio = calcular_promedio(cantidades)
    maximo = buscar_maximo(cantidades)
    minimo = buscar_minimo(cantidades)
    
    indice_max = cantidades.index(maximo)
    nombre_max = nombres[indice_max]
    
    awa()
    print("=== RESULTADOS ===")
    print(f"Total de libros prestados: {total}")
    print(f"Promedio de libros prestados: {promedio:.2f}")
    print(f"Mayor cantidad prestada: {maximo}")
    print(f"Menor cantidad prestada: {minimo}")
    print(f"Lector con mayor préstamo: {nombre_max}")
    awa()
#SALIDA:

nombres, cantidades = leer_prestamos()
mostrar_resultados(nombres, cantidades)
