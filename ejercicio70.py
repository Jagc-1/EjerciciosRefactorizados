#Algoritmo que muestre el promedio de 3 notas y muestre si esta aprobado o desaprobado.


nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 3.5:
    print("El promedio es", promedio,"asi que esta aprobado")
else:
    print("El promedio es", promedio,"asi que esta reprobado")
