#Algoritmo que muestre la unidad, la decena y la centena
print("Ingrese Nro de 3 cifras..")
n = int(input())

cen = (n -(n % 100))/100
res =  n % 100
dec =  (res - (res % 10))/10
uni =  res % 10

print("----------------------")
print("Centena: ", cen)
print("Decena: ", dec)
print("Unidad: ", uni)
print("----------------------")
