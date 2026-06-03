print("="*50)
#definicion de lista:
a= int(input("Seleccione el número  1 ==> "))
b= int(input("Seleccione el número  2 ==> "))
c= int(input("Seleccione el número  3 ==> "))
d= int(input("Seleccione el número  4 ==> "))
e= int(input("Seleccione el número  5 ==> "))
lista=[a, b, c, d, e]
#2. Mostrar la lista completa:

print("Lista de números: ", lista)
print("="*50)
#3. Recorrer la lista
for a in lista:
    print(a)
print("="*50)

#4. Operaciones Estadísticas:
suma= sum(lista)
maximo= max(lista)
minimo= min(lista)
promedio=sum(lista)/len(lista)
cantidad=len(lista)

#5. Mostrar resultado:
print(suma)
print(maximo)
print(minimo)
print(promedio)
print(cantidad)

print("="*50)

print("ELABORADO POR ESTEBAN TRINIDAD")

print("="*50)
