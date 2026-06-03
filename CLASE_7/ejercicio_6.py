#Pedro tiene un ahorro en banco, el banco le ofrece un interés anual de 9%.
#El programa clacula los intereses ganados y pregunta si conviene reinvertido.
#Si supera los $7000 soles.

#Listas[]
#FV= Pv(1+i)**n

#ENTRADA:
print("="*50)

capital = int(input("Ingrese el número de ahorro ==>  "))
i = float(input("Ingrese la tasa en años (con decimales) ==>  "))
n= int(input("Ingrese el número de años ==>  "))
#PROCESO:
print("="*50)

limite = 7000
total = capital * (1 + i) ** n
interes = total - capital

print(f"Ahorro que posees: S/ {capital:.2f}")
print(f"Interés ganado:  S/ {interes:.2f}")
print(f"Total acumulado: S/ {total:.2f}")

#SALIDA:
print("="*50)
if total > limite:
    print("Si conviene reinvertir vro.")
else:
    print(f"No conviene reinventir vro. Te Falta: S/ {limite - total:.2f}")

print("="*50)
print("ELABORADO POR ESTEBAN TRINIDAD")
print("="*50)
