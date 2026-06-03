# Diseñe un algoritmo donde se solicite al usuario que introduzca una letra ‘S’ o ‘N’ 
# hasta que lo haga correctamente. Luego muestre la opción introducida por el usuario.

#Entrada:
print("="*50)
print(" => Bienvenido al programa de validación de letras") 
print("="*50)

letra = input("Introduce una letra 'S' o 'N': ")
#Proceso:
while letra != 'S' and letra != 'N':
    print("Letra incorrecta. Por favor, introduce 'S' o 'N'.")
    letra = input("Introduce una letra 'S' o 'N': ")
#Salida:
print("Has introducido la letra: ", letra)
print("="*50)
print(" => Elaborado por Trini")
print("="*50)
