#Algoritmo que muestre el factorial de un número ingresado

fac = 1

print("Ingrese el número a calcular el factorial: ")
num = int(input(":)"))
print("Serie factorial: ")

for x in range(1, num + 1):
    print((num + 1) - x, end=" ")
    fac = fac * x
print(f"\nEl Factorial de {num} es: {fac}")
