#ALGORITMO QUE MUESTRA EL TRIÁNGULO DE PASCAL

print("-- Mostrar Triangulo De Pascal --")
print("Ingrese Dimension [Menos o igual a 20]: ")
N = int(input(":)"))
print("---------------------")

for izq in range(N):
    cont = 1

    for espacio in range(N - izq):
        print(" ", end='')

    for der in range(izq + 1):
        print(cont, end=' ')
        cont = cont * (izq - der) // (der + 1)
    print()
