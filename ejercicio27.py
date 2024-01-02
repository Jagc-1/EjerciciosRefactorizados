#Algoritmo que muestra los números primos desde 1 hasta N números ingresados

print("ingrese un valor: ")
n = int(input(":)"))

for cont in range(1, n+1):
    divisible = 0
    for divi in range(1,cont+1):
        if cont % divi == 0:
            divisible += 1
    if divisible == 2:
        print(cont, end=" ")
