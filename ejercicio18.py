#Algoritmo que muestra si un número es o no capicúa


print("-----------")
print("Ingrese un número: ")
num = input(":)")

revNum = num[::-1]

print("-----------")
print(f"Número ingresado: {num}")
print("-----------")
print(f"Número al revés: {revNum}")
print("-----------")

if num == revNum:
    print("El número ingresado es capicúa")
else:
    print("El número ingresado no es capicúa")
