# Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y
# luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté
# comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de
# piezas aptas que hay en el lote.

#Entrada:
while True:
    print("="*50)
    print("=== BIENVENIDO AL CONTROL DE PIEZAS ===")
    print("="*50)

    n=int(input("Ingrese la cantidad de piezas del lote: \n Su repuesta => "))

    print("="*50)
    aptas=0
    for a in range (1, n+1):
        long= float(input(f"INGRESE LA LONGITUD DE LA PIEZA {a}: \n Su repuesta =>  "))
        if 1.20 <= long <= 1.30:
            aptas+=1
    print("="*50)
    print(f"\n la cantidad de piezas aptas en el lote son: {aptas} ")
    print("="*50)
    rpta=input("¿Deseas hacer otro control? (si/no): \n Su repuesta =>  ").lower().upper()
    if rpta.lower().upper() != "si":
        print("="*50)
        print("=== ¡GRACIAS POR USAR EL PROGRAMA ===")
        print("="*50)
        break
print("ELABORADO POR ESTEBAN TRINIDAD")