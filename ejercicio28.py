# Algoritmo que muestra si un número ingresado es primo


print("-----------------")
print("ingrese un valor: ")
num = int(input(":)"))
print("-----------------")

divisible = 0

for divi in range(1, num+1):
    if num % divi == 0:
        divisible += 1
if divisible == 2:
    print("Es primo")
else:
    print("No es primo")
