#Algoritmo que calcule el IVA del monto total a pagar

print("-- IVA --")

print("Costo de la casa: $")
c = int(input(":)"))

print("Valor del IVA: %")
iva = int(input(":)"))

total = (c + (c * (iva/100)))

print("IVA de: ",iva,"% :",(c * (iva/100)))
print("Total a pagar: $",total)
