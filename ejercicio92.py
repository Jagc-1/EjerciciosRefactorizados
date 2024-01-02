#Hacer un algoritmo que muestre el monto a pagar según el tipo de seguro elegido [X - Y - Z]


print('-- Bienvenido, aqui sabras el precio a pagar según el tipo de seguro elegido --')
print('1. X')
print('2. Y')
print('3. Z')

seguro = int(input('Seleccione un seguro: '))

if seguro == 1:
    print('Costo Mensual $45')
elif seguro == 2:
    print('Costo Mensual $30')
elif seguro == 3:
    print('Costo Mensual $15')
else:
    print('Opcion invalida')
