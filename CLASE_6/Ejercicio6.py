# Programa que almacena cursos en una lista y los muestra en pantalla:
# Usando f-strings:

# 1. Lista de Cursos:
lcursos=["Matemáticas", "Física", "Química", "Historia", "Lengua", "Biología"]

# 2. Lista de Notas:
lnotas=[]

print("="*50)
print("Ingreso de Notas")

for curso in lcursos:
    pregunta=f"¿Qué nota sacaste en {curso}? "
    nota=input(pregunta)
    lnotas.append(nota)

print("="*50)
print("La lista de notas es:", lnotas)

# Mostrar información curso y nota:

for i in range(len(lcursos)):
    print(f"En {lcursos[i]} has sacado {lnotas[i]} ")

print("="*50)
print("Proceso finalizado")   

