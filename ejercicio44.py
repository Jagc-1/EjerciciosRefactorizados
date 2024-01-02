#Algoritmo que muestre cuantas entradas al cine se pueden comprar con un monto ingresado.
monto = 1000

print("Nro de Meses: ")
meses = int(input())

intereses = round(monto * (meses * 0.02))
totalP = round(monto + intereses)

print("-----------------------")
print("Intereses: ", intereses)
print("Total a Pagar: ", totalP)
print("-----------------------")
