# La pizzería Bella Nona ofrece pizzas vegetarianas y no vegetarianas a sus
# clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# • Ingredientes vegetarianos: Pimiento y anchoveta
# • Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
# en función de su respuesta le muestre un menú con los ingredientes disponibles para
# que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate
# que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida
# es vegetariana o no y todos los ingredientes que lleva.

#Entrada:
while True:
    print("="*80)
    print("=== BIENVENIDO A LA PIZZERIA BELLA ===")
    print("="*80)
    tipo=input("¿Desea una pizza vegetariana? (si/no) \n Su repuesta =>  ").lower()
    if tipo == "si":
        print("="*80)
        print("1. Pimiento")
        print("2. Anchoveta")
        opcion = int(input("Elija un ingrediente (1 - 2): \n Su repuesta => "))

        print("="*80)
        if opcion ==1:
            ingrediente= "Pimiento"
        elif opcion==2:
            ingrediente= "anchoveta"
        else:
            print("Opción no válida")
            ingrediente=None
        tipo_pizza = "Vegetariana"

    elif tipo == "no":
        print("="*80)
        print("\n === INGREDIENTES NO VEGETARIANOS === ")
        print("="*80)
        print("1. Pepperoni")
        print("2. Jamón")
        print("3. Salmón")
        print("="*80)
        opcion= int(input("\n Elija un ingrediente (1 -3): \n su repuesta =>  "))
    
        print("="*80)
        if opcion== 1:
            ingrediente= "pepperoni"
        elif opcion == 2:
            ingrediente= "Jamón"
        elif opcion ==3:
            ingrediente= "salmón"
        else:
            print("Opción no válida")
            ingrediente=None
        tipo_pizza = "NO VEGETARIANA"
    else:
        print("opción no válida")
        ingrediente= None
        tipo_pizza=None
    if ingrediente and tipo_pizza:

        print ("Resumen del pedido")
        print("="*80)
        print(f"Tipo de pizza: {tipo_pizza}")
        print(f"Ingredientes: Mozzarella, tomate,{ingrediente}")
        print("="*80)
    rpta= input("¿Deseas volver hacer otro pedido? (si/no): \n Su repuesta:").upper().lower()
    if rpta.lower() != "si":
        print("="*80)
        print("¡GRACIAS POR USAR EL PROGRAMA!")
        print("="*80)
        break

    print("Elaborado por Esteban Trinidad")