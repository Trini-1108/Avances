# Uso de def:
print("="*50)

print("=== CALCULADORA ===")

print("="*50)

def suma (a,b):
    return a+b
def resta (a,b):
    return a-b
def multiplicacion (a,b):
    return a*b
def division (a,b):
    return a/b
def potencia (a,b):
    return a**b
def resto_entero(a,b):
    return a%b

#asignar valores:
a= int(input("INGRESE UN PRIMER NÚMERO: \n SU RESPUESTA =>   "))
b= int(input("INGRESE UN SEGUNDO NÚMERO: \n SU RESPUESTA =>   "))

print("="*50)

import time
time.sleep (1)


#SALIDA:
print("SUMA: ", suma(a,b))
print("RESTA: ", resta(a,b))
print("MULTIPLICACION: ", multiplicacion (a,b))
print(f"DIVISION: {division(a,b):.3f}")
print("POTENCIA: ", potencia(a,b))
print("RESTO ENTERO: ", resto_entero(a,b))
print("="*50)


