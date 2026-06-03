#CADENAS:

cadena1 ="Quien mal anda, mal acaba"
print(cadena1.replace("mal","bien")) #Reemplaza "mal" por "bien"
print(cadena1.replace("mal","bien",1)) #Reemplaza solo la primera ocurrencia de "mal" por "bien"

x="Programa en Python"
print(x.split())
email="martin.vasquezz@gmail.com"
print(email.split("@"))

texto = "     Hola Python      "
print(texto.lstrip()) #elimina elementos a la izquierda
print(texto.rstrip()) #elimina elementos a la derecha
print(texto.strip()) #elimina a ambos lados

fecha = "2026 - 05 - 25"
print(fecha.split("-"))

datos="Ana, 25, Madrid"
nombre, edad, ciudad = datos.split(",")
print(nombre, edad, ciudad)
