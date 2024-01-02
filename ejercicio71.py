#Algoritmo que muestre si un número es par o impar


print("Ingrese número: ")
numero = int(input(":)"))

c = numero // 2
r = c * 2
re = numero - r

if re == 0:
    print("El número es par")
else:
    print("El número es impar")
