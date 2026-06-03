# Un profesor tiene un salario inicial de $1500,
# Recibe un incremento de 10 % anual durante 6 años. 
# ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años?, USA WHILE

#Entrada:
print("="*50)
salario_inicial = int(input("Ingrese el salario inicial= "))
incremento_anual = float(input("Ingrese el incremento anual sin porcentaje= "))/100
años = int(input("Ingrese el número de años= "))
print("="*50)
#Proceso:
salario_inicial = salario_inicial * (1+incremento_anual)**años
salario_anual= salario_inicial
contador = 1
while contador <=años:
    salario_anual = salario_anual / (1+incremento_anual)
    print(f"Salario del años {contador}: {salario_anual:.2f}")
    contador= contador + 1

#Salida:
print("="*50)
print(f"salario al cabo de {años} años: {salario_anual:.2f}")
print("="*50)
print("Elaborado por Trini")
print("="*50)
