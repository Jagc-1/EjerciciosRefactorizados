#Algoritmo que muestre el descuento a pagar según el monto de compra en un supermercado.
import random
descuento = 0
compra  = 0

print('Cantidad Compra: ')
compra = int(input(':)'))

color = random.randint(1, 5)

if color == 1:
    print('Color Blanco')
    descuento = 0.1
elif color == 2:
    print('Color Verde')
    descuento = 0.05
elif color == 3:
    print('Color Negro')
    descuento = 0.04
elif color == 4:
    print('Color Celeste')
    descuento = 0.05
elif color == 5:
    print('Color Rojo')
    descuento = 0

print('Descuento: ', descuento)
print('Importe Descuento: ', compra * descuento)
print('Total a pagar: ', compra - (compra * descuento))
