# Programa que almacena cursos en una lista y los muestra en pantalla:

lcursos=["Matemáticas", "Física", "Química", "Historia", "Lengua", "Biología"]

lnotas=[]

print("="*50)
print("INGRESO DE NOTAS")

for curso in lcursos:
    pregunta="¿Qué nota sacaste en {}? ".format(curso)
    nota=input(pregunta)
    lnotas.append(nota)

print("="*50)
print("La lista de notas es: ", lnotas)

