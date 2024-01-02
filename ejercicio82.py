#Algoritmo que calcule el IGV 18% del monto a pagar, si el monto es mayor a $500.


print("Ingrese Monto: ")
num = int(input())

if num > 500:
    print('IGV 18%: ', (num * 0.18))
