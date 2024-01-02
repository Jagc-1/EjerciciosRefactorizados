#Calcula el monto a pagar por 10 compras realizadas


for cont in range(10):
    cont +=1
    print("-------------------")
    print("Consumo",cont,": $.",  )
    cons =  float(input(":)"))
    total = total + cons
    if total > 50.000:
        des = total * 0.07

print(f"Consumo Total: ${total:.3f}")
print(f"Descuento aplicado: ${des:.3f}")
print(f"Valor Total a Pagar: ${total-des:.3f}")
