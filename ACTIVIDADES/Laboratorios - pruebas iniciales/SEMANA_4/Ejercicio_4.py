# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la
# semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por
# las horas trabajadas, usando while.

#Entrada:
print("="*50)
print("Ingrese las horas trabajadas por día durante la semana= ")
print("="*50)

#Proceso:
total_horas = 0
dia = 1
while dia <=6:
    horas = float(input("Día {}: ".format(dia)))
    total_horas= total_horas+horas
    dia+=1
    sueldo = total_horas * 15
#Salida:
print("="*50)
print("Total de horas trabajadas en la semana= ", total_horas)
print("Sueldo a recibir por las horas trabajadas= ",sueldo)
print("="*50)
print("Elaborado por Trini")
print
("="*50)
