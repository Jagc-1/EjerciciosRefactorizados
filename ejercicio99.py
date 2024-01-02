#Calcular el monto a pagar por la compra de teclados, el precio varia según su cantidad.


print('Ingrese la cantidad a comprar: ')
cant = int(input(':)'))

if cant in [1,2,3]:
    precio = 15
elif cant in [4,5,6,7,8]:
    precio = 11
else:
    precio = 10


print('Costo por teclado: $', precio)
print('Total a pagar: $', cant * precio)
