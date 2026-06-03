#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla loque tiene que pagar

#Entrada:
while True:
    print("="*80)
    print("=== BIENVENIDO AL PROGRAMA ===")
    print("="*80)

    renta= int(input("INGRESE SU RENTA ANUAL QUE PUEDE GENERAR: \n Su repuesta =>  "))

    if renta < 10000:
        impuesto = renta * 0.05
    elif 10000 >= renta <= 20000:
        impuesto= renta * 0.15
    elif 20000 > renta <=35000:
        impuesto=renta * 0.20   
    elif 35000 > renta <= 60000:
        impuesto= renta * 0.30
    else:
        impuesto=renta* 0.45

    print("="*80)

    print(f"Lo que tiene que pagar en impuesto es: \n S/. {impuesto:.2f}")

    print("="*80)
    rpta=input("¿Deseas hacer otra operación? (si/no): \n SU REPUESTA: ")
    rpta.lower() != "Si"
    print("="*80)
    print("¡GRACIAS POR USAR EL PROGRAMA!")
    print("="*80)
    break
