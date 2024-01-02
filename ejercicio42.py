#Algoritmo que ingrese un total de segundos y muestre cuantas horas, minutos y segundos hay.


print("Ingrese cantidad de segundos: ")
xsegundos = int(input())

horas = xsegundos // 3600
minutos = ((xsegundos - (horas * 3600))/60)
segundos = ((xsegundos - (horas * 3600)+ (minutos * 60)))

print("-----------------------------------")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")
print("-----------------------------------")
