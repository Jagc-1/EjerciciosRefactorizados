#Algoritmo que calcule el salario a pagar de un empleado, con un descuento del 20%.


print("Inngrese Su Salario: ")
salario = int(input())

descuento = salario * 0.20
salarioFinal = salario - descuento

print("-----------------------------------")
print("Descuento del 20: ", descuento)
print("Su Salario Final es: ", salarioFinal)
print("-----------------------------------")
