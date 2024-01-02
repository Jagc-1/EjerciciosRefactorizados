#Algoritmo que calcule las medidas de una pared según el alto y largo ingresado.

print("Ingrese el alto de la pared(metros): ")
high = float(input())

print("Ingrese el ancho de la pared(metros): ")
withP = float(input())


arena = ((high * withP) * 0.25)

print("-----------------------")
print(f"La arena necesaria son: {arena} mt3")
print("-----------------------")
