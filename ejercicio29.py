#Algoritmo que muestra la cantidad de números pares e impares ingresados

sumal = 0
sumaP = 0


num = int(input("INGRESE NUMERO: "))

for x in range(1, num+1):
    if x % 2 == 0:
        sumaP += x
    else:
        sumal += x

print("Suma de pares:", sumaP)
print("Suma de impares:", sumal)
