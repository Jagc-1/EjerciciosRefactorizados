#Algoritmo que calcule el descuento a pagar según el monto de compra


print('Monto de compra: ')
monto = float(input())

if monto > 350:
    descuento = monto * 0.35
    print('El descuento es: ', descuento)
else:
    descuento = monto * 0.10
    print('El descuento es: ', descuento)

print('Monto a pagar: ',(monto-descuento))
