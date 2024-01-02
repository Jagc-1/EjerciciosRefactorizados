#Algoritmo que muestre el sueldo a pagar de un empleado según su categoría.

bonificacion = 0

print('Sueldo Base: ')
sueldoB = float(input(':)'))

print('Categoria: 1.A - 2.B - 3.C - 4.D')
categoria = int(input('Categoria: '))

if categoria == 1:
    bonificacion = sueldoB * 0.1
elif categoria == 2:
    bonificacion = sueldoB * 0.2
elif categoria == 3:
    bonificacion = sueldoB * 0.3
elif categoria == 4:
    bonificacion = sueldoB * 0.5
else:
    print('Opcion invalida')

print('BONIFICACION: ', bonificacion)
print('SUELDO NETO: ', sueldoB + bonificacion)
