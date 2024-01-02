#ALGORITMO QUE MUESTRE EL SUELDO DE UN TRABAJADOR
boni = 0
sueldoF = 0

print('Ingrese nombre: ')
nombre = input()
print('Ingrese sueldo basico: ')
salario = float(input())
print('Nro de hijos: ')
hijos = int(input())

if hijos > 0:
    boni = salario * 0.7


sueldoF = salario + boni

print('Binificación: ', boni)
print('El sueldo Final es: ', sueldoF)
