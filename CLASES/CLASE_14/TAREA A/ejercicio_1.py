#ENTRADA:

def aña(simbolo ="=", longitud=50):
  print(simbolo*longitud)

def analizar_notas(lista):
    notas_aprobatorias = 0
    notas_desaprobatorias = 0

    #PROCESO:
    if not lista: 
        return 0, 0, None, None 
    nota_mayor = max(lista)
    nota_menor = min(lista)
    for nota in lista:
        if nota >= 11:
            notas_aprobatorias += 1
        else:
            notas_desaprobatorias += 1
            
    return notas_aprobatorias, notas_desaprobatorias, nota_mayor, nota_menor

#PROCESO:

aña()
a=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
b=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
c=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
d=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
e=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
f=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
h=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
i=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
j=int(input("Ingrese un número cualquiera= \n Su Repuesta =>  "))
notas_ejemplo = [a,b,c,d,e,f,h,i,j]
aña()

cant_aprobadas, cant_desaprobadas, max_nota, min_nota = analizar_notas(notas_ejemplo)

#SALIDA: 

aña()
print(f"Lista de notas: {notas_ejemplo}")
print(f"Cantidad de notas aprobatorias: {cant_aprobadas}")
print(f"Cantidad de notas desaprobatorias: {cant_desaprobadas}")
print(f"Nota mayor: {max_nota}")
print(f"Nota menor: {min_nota}")
aña()
