# Nave Espacial:)
# Tiene 100 unidades de energía
#Explor un planeta: Consume 20
#Escender motores: Consume 30
#Activar escudo: consume 15
#Salir.

#Entrada:
energia=100

#Proceso:
while energia >0:
    print("Energia disponible:" ,energia)
    print("1. Explorar planeta (20 de energía)")
    print("2. Escender motores (30 de energía)")
    print("3. Activar escudo (15 de energía)")
    print("4. Terminar mision")

    opcion=int(input("Seleccione una opcion: "))

    print("="*50)

    if opcion == 1:
        energia= energia-20
        print("exploracion completada")
    elif opcion == 2:
        energia= energia-30
        print("motor escendido")
    elif opcion == 3:
        energia=energia-15
        print("escudo activado")
    elif opcion== 4:
        print("Terminamos la mision, felicidades")
        break
    else:
        print("Seleccione un numero del 1 al 4 por favor")

print("Fin de la mision.")

print("="*50)

print("El proyecto fue elaborado por Esteban Trinidad")

