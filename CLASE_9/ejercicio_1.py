#Uso de funciones (subbrutinas)

#Definiendo una función:
print("="*50)

def saludar():
    print("===HOLA; BIENVENIDO A PYTHON===")

#INVOCAR LA FUNCIÓN:
saludar()

print("="*50)

import time
time.sleep(1.5)


#DEFINIENDO LA FUNCIÓN CON PARÁMETROS:
def saludar(nombre):
    print(F"=== Hola, {nombre} ===")
saludar("José")

print("="*50)

import time
time.sleep (1.5)

#FUNCIÓN QUE RETORNA UN VALOR:

def saludarMundo():
    return "HOLA MUNDO"
print(saludarMundo())

import time
time.sleep(1.5)

print("="*50)

#Función con parámetro y retorno:
a=int(input("INGRESE UN PRIMER NÚMERO: \n"))

b= int(input("INGRESE UN SEGUNDO NÚMERO: \n"))

def suma(a,b):
    return a+b
resultado=suma(a,b)
print(f"===El resultado es: {resultado} ===")

print("="*50)


