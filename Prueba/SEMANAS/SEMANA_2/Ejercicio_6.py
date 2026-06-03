# Estructura de control selectiva simple:

#1° Ingreso:

print("_"*80)
print("Setencia condicional simple")
print("="*80)
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
msg="No se encontró resultado"

#2° Proceso

if b>a:
    msg="b es mayor que a" # type: ignore

#3 Salida:

print("_"*80)
print("Resultado")
print("="*80)
print(msg)
print("Elaborado por Trini")
