#Algoritmo que calcule la bonificación a pagar


print('Ingrese el monto de venta: ')
venta = int(input())

if venta > 2000:
    print('Bonificación del 10%: $', venta * 0.10)
else:
    print('Bonificación del 50%: $', venta * 0.50)
