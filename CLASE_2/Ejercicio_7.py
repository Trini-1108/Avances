# Estructura de control selectiva simple:

#1° Ingreso:

print("="*80)
print("Setencia condicional Multiple")
print("="*80)
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
msg="No se encontró resultado"

#2° Proceso

if b > a:
    msg="b es mayor que a" 
elif b==a:
    msg="b es igua que a"
else:
    msg="b es menor que a" 

#3°- Resultados
print("="*80)
print("Resultado")
print("[]"*80)

print(msg)
print("Elaborado por Trini")
print("="*80)
