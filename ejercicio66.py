#Algoritmo que dibuje un triangulo con un carácter ingresado

print("Ingrese la Altura: ")
alt = int(input())

print("Ingrese Caracter: ")
caracter = input()

for i in range(alt):
    for j in range(alt - i):
        print(" ", end="")

    for j in range(2*i - 1):
        print(caracter, end="")
    print()
