#Algoritmo que muestra el promedio de varias notas ingresadas


suma = 0
print("Ingrese la cantidad de notas: ")
n =  int(input(":)"))
print("------------------------------")
for cont in range(1,n +1):
    print(f"Nota {cont}: ")
    nota = float(input(":)"))
    print("-------------------------")
    suma += nota
prom = suma/n
print("El promedio es: {:.1f}".format(prom))
