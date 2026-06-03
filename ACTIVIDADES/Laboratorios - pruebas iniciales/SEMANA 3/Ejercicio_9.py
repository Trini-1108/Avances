# Desarrolle un algoritmo que permita convertir calificaciones numéricas 
# según la siguiente tabla: A = 19 y 20, B =16, 17 y 18, C = 13, 14 y 15, D = 10, 11 y 12, E = 1 hasta el 9. 
# Se asume que la nota está comprendida entre 1 y 20. 
# Usar el comando SEGÚN.

#Entrada:
print("=" * 100)
nota= int(input("Ingrese una nota númerica entre el 1 hasta el 20: "))
print("=" * 100)

#proceso:
if nota >= 19 and nota <=20:
    print ("La nota que usted ingreso es A")
elif nota <=18 and nota >=16:
    print("La nota que ingreso usted es B")
elif nota <=15 and nota >=13:
    print("La nota que ingreso es C")
elif nota <=12 and nota >=10:
    print("La nota que ingreso es D")  
else:
    print("La nota que ingreso es E")

#ANOTACION: A la hora de comparar numeros, se tiene que poner la misma palabra dos veces:
#Ejemplo: nota >= 19 and nota <=20, no se puede poner nota >= 19 and <=20, porque el programa no lo va a entender.
#Salida:
print("El proyecto fue elaborado por: Trinidad Esteban")