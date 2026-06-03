# Programa que almacena cursos en una lista y los muestra en pantalla:

# 1. Lista de Cursos:
lcursos=["Matemáticas", "Física", "Química", "Historia", "Lengua", "Biología"]

# 2. Lista de Notas:
lnotas=[]

print("="*50)
print("Ingreso de Notas")

for curso in lcursos:
    pregunta="¿Qué nota sacaste en {}? ".format(curso)
    nota=input(pregunta)
    lnotas.append(nota)

print("="*50)
print("La lista de notas es:", lnotas)

# Mostrar información curso y nota:

for i in range(len(lcursos)):
    print("En {} has sacado {} ".format(lcursos[i], lnotas[i]))

print("="*50)
print("Proceso finalizado")   

