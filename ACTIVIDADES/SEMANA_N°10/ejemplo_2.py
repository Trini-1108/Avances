# Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos
# ingresos superiores a 1000 soles mensuales. Escribir un programa que pregunte al usuario
# Su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

#Entrada:
while True:
    print("="*80)
    print("=== BIENVENIDO AL PROGRAMA ===")
    print("="*80)

    edad= int(input("INGRESE LA EDAD QUE POSEE USTED: \n SU REPUESTA=>  "))

    ingreso= int(input("INGRESE EL INGRESO MENSUAL QUE USTED GENERA: \n Su Repuesta => "))

    if edad>=18 and ingreso>=1000:
        print("USTED DEBE TRIBUTAR AL ESTADO")
    else:
        print("USTED NO DEBE TRIBUTAR PARA EL ESTADO")
    print("="*80)
    rpta=input("¿Desea hacer otra operación? (si/no): \n SU REPUESTA => ")
    if rpta.lower() != "si":
        print("="*80)
        print("¡GRACIAS POR USAR EL PROGRAMA!")
        print("="*80)
        break
