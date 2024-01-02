#Algoritmo que muestre la serie : 1 + 2/3 + 3/5 + 4/7 usando FOR.

suma = 0
d = 1

print("Valor de N: ")
n = int(input(":)"))

for i in range(1, n + 1):
    if i == n:
        print(f"{i}/{d}")
    else:
        print(f"{i}/{d} + ", end="")
    suma = suma + (i / d)
    d = d + 2

print(f"La suma es: {suma}")
