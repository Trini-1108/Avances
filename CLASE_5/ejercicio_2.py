# Ingrese sus notas usando "for"
print("="*100)
print("Ingere la nota del alumno")
print("="*100)

#ENTRADA:
notas= int(input("¿CUANTAS NOTAS DESEAS INGRESAR?: "))
suma= 0

#PROCESO:
for a in range(notas):
    num= float(input("Ingrese nota= "))
    suma= num+1

promedio=suma/notas

#SALIDA:
print("="*100)
print(f"La suma de notas es= {suma:.0f}")
print(f"EL PROMEDIO DE LAS NOTAS ES= {promedio:.2f} ")
print("="*100)
print("ELABORADO POR ESTEBAN TRINIDAD")