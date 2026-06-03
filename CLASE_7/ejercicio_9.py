#Evaluacion de crédito personal:

#1. Entrada:
print("="*50)

sueldo= float(input("INGRESE SUELDO MENSUAL:  "))

print("Tipo de vivienda")
print("1. vive con parientes")
print("2. Vivienda alquilada")
print("3. Vivienda propia")

vivienda=int(input("Seleccione una opción (1 - 3):  "))
tarjeta= input("¿Tienes tarjeta de crédito? (SI/NO) ==>  ").lower()
carga= input("¿Tiene carga familiar? (SI/NO): ").lower

#2. Proceso:
puntaje=0

#Evaluación de sueldo: 
if sueldo <1500:
    puntaje+=6
elif sueldo >=1500 and sueldo<=6000:
    puntaje+=12
else:
    puntaje+=10

#Evaluzación del tipo de vivienda:
if vivienda == 1:
    puntaje+=2
elif vivienda ==3:
    puntaje+=5
elif vivienda==3:
    puntaje+=10
else:
    print("Tipo de vienda no válida")
#Evaluación de tarjeta de crédito:
if tarjeta=="si":
    puntaje+=6
else:
    puntaje+=3

#3. Salida:
print("="*50)
print("Resultado de la evaluación")
print("puntaje obtenido:  ", puntaje)
if puntaje >=20:
    print("APROBADO!!")
else:
    print("DESAPROBADO")

print("="*50)
