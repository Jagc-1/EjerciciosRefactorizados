#Algoritmo que dibuje un rombo de asteriscos
altura = int(input("Ingrese la altura del rombo: "))

for i in range(1, altura + 1):
    print(" " * (altura - i) + "*" * (2 * i - 1))


for i in range(altura - 1, 0, -1):
    print(" " * (altura - i) + "*" * (2 * i - 1))
