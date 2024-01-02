#Algoritmo que busque un número que se ha generado de forma aleatoria


import random
sw = 0
numA = random.randint(1, 20)

for i in range(3):
    print("----------------------------------")
    print("Encientre el número entre [1-20]: ")
    num =  int(input(":)"))
    print("----------------------------------")
    if num == numA:
        print("¡Felicidades!. Has encontrado el número")
        sw = 1
        i = 3
    else:
        if num > numA:
            print("Ingrese un número más bajo")
            break
        else:
            print("Ingrese un número más alto")

    if sw == 0:
        print("Has perdido")
        print(f"El número a encontrar era: {num}")
        break
