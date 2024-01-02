#Algoritmo que calcule el IGV si el monto de compra es mayor a $100 USA
igv = 0
monto  = 0

print("Ingrese Precio: ")
precio = float(input())
print('Ingrese cantidad: ')
cant = int(input())

monto = precio * cant

if monto > 100:
    igv = monto * 0.18


print('Total: ',monto)
print("IGV 18%: ", igv)
print('Total a pagar: ', (monto + igv))
