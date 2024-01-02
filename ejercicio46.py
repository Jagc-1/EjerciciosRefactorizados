#Algoritmo que al ingresar las horas, minutos y segundos, calcule el costo total.

print("Ingrese las horas: ")
h = int(input())

print("Ingrese los minutos: ")
m = int(input())

print("Ingrese los segundos: ")
s = int(input())

costo = ((h * 3600) +(m * 60) + s) * 0.25
print("----------------------")
print("Costo total: ", costo)
print("----------------------")
