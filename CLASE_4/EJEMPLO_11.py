# CAJA AUTOMATICA.
#Saldo inicial = 1000
#programa pregunta cuanto desea retirar.
# programa donde funcionará cuando el saldo >0
#Mostrar Saldo restante
# Preguntar si desea hacer otra operacion.

#Entrada:
saldo = 1000

#proceso:
print("="*50)

while saldo>0:
    print("Saldo disponible:", saldo)
    retiro=int(input("¿Cuánto dinero desea retirar?: "))
    if retiro<=saldo:
        saldo=saldo-retiro
        print("retiro exitoso")
    else:
        print("Fondos insuficientes")
    print("="*50)
    
    continuar=input("Desea realizar otra operación? (si/no): ")

    if continuar =="no":
        break

print("Gracias por usar el cajero :D")

print("="*50)