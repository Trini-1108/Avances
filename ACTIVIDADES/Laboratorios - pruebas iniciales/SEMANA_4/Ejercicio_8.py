# Desarrolle un algoritmo para la empresa Constructora “VivirBien”
# Que le permita calcular e imprimir la nómina para su cancelación a un total de 50 obreros calificados 
# A quienes debe cancelar por horas trabajadas. 
# La hora trabajada se pautó en 30 soles.
# El algoritmo debe permitir ingresar el nombre del obrero, las horas trabajadas y luego calcular el pago a cancelar.
# Al finalizar el proceso de ingreso de datos, el algoritmo debe imprimir el total a cancelar por cada obrero y el total a cancelar por los 50 obreros.
# Definir el costo por hora
costo_por_hora = 30
# Inicializar el total a cancelar por todos los obreros
total_a_cancelar = 0
# Ciclo para ingresar datos de 50 obreros
print("="*50)
print("NÓMINA DE OBREROS - CONSTRUCTORA VIVIRBIEN")
print("="*50)

for i in range(1, 51):
    # Ingresar el nombre del obrero
    nombre_obrero = input(f"Ingrese el nombre del obrero {i}: ")
    # Ingresar las horas trabajadas
    horas_trabajadas = int(input(f"Ingrese las horas trabajadas por {nombre_obrero}: "))
    # Calcular el pago a cancelar
    pago_a_cancelar = horas_trabajadas * costo_por_hora
    # Imprimir el pago a cancelar por el obrero
    print(f"El pago a cancelar por {nombre_obrero} es: {pago_a_cancelar} soles")
    # Acumular el total a cancelar por todos los obreros
    total_a_cancelar += pago_a_cancelar
print("="*50)

# Imprimir el total a cancelar por los 50 obreros
print(f"El total a cancelar por los 50 obreros es: {total_a_cancelar} soles")
print("Elaborado por Trini")