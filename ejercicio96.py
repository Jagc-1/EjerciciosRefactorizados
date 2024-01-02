#Algoritmo que muestre el total a pagar por la compra de teclados

cantidad = 5

print('Cantida Compra: ')
cantidad = int(input(':)'))

if cantidad in [1, 2, 3]:
    costo = 15
elif cantidad in [4, 5, 6]:
    costo = 11
else:
    print('Opcion invalida')

print('Costo por teclado: ', costo)
print('Total a pagar: ', cantidad * costo)
