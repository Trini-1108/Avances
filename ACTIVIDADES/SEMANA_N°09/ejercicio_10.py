#Entrada:
while True:
    nombre= input("INGRESA TU NOMBRE COMPLETO: \n Su repuesta =>  ")

    print("="*80)
    print(f"\n En Minúsculas: {nombre.lower()}")
    print(f"\n En Mayúsculas: {nombre.upper()}")
    print(f"\n Capitalizado: {nombre.capitalize()}")
    print("="*80)

    rpta=input("\n ¿Deseas hacerlo de nuevo? (si/no): \n Su repuesta => ").lower().upper()
    if rpta != "si":
        print("="*80)
        print("¡GRACIAS POR USAR EL PROGRAMA!")
        print("="*80)
        break
print("Elaborado por Esteban Trinidad")
print("="*80)