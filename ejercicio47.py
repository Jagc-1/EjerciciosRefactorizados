#Algoritmo que muestre los días transcurridos desde el inicio del año hasta ahora

print("Nro del Mes: ")
month = int(input())

print("Nro de dias: ")
days = int(input())

tiempo = (((month - 1) * 30) + days)

print("----------------------")
print("Dias transcurrido: ", tiempo)
print("----------------------")
