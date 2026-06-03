# Programa que almacena cursos en una lista y los muestra en pantalla:

lcursos=["Matemáticas", "Física", "Química", "Historia", "Lengua", "Biología"]

lnotas=[]

print("="*50)
print("INGRESO DE NOTAS")

for curso in lcursos:
    pregunta=f"¿Qué nota sacaste en {curso} ? => "
    nota=input(pregunta)
    lnotas.append(nota)

print("="*50)
print("La lista de notas es: ", lnotas)
print("="*50)

#Mostrar información curso:

for a in range(len(lcursos)):
    print(f"En {lcursos[a]} has sacado {lnotas[a]} ")

print("="*50)
print("Proceso finalizado")
