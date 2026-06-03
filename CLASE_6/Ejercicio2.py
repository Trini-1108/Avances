# Algunos comandos usados en Listas:

# Lista inicial de frutas:
#            0         1         2       3
lfrutas=["manzana","platano","cereza","piña"]
#          -4         -3        -2      -1

# Añadir un elemento al final de la lista (append):
lfrutas.append("uva")
print(lfrutas)

print("="*50)

# Insertar un elemento en un índice específico:
lfrutas.insert(1,"naranja")
print(lfrutas)

print("="*50)

# Eliminar un elemento específico:
lfrutas.remove("uva")
print(lfrutas)

print("="*50)

# Eliminar un elemento por índice:
lfrutas.pop(1)
print(lfrutas)

print("="*50)

# Invertir el orden de la lista:
lfrutas.reverse()
print(lfrutas)

print("="*50)

# Ordenar alfabeticamente:

lfrutas.sort()
print(lfrutas)

print("="*50)
# Invertir el orden de la lista:

lfrutas.sort(reverse=True)
print(lfrutas)
