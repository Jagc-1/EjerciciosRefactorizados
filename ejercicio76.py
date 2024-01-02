#Algoritmo que muestre el número intermedio de tres números ingresados

print('Ingrese el primer número: ')
n1 = int(input())

print('Ingrese el segundo número: ')
n2 = int(input())

print('Ingrese el tercer número: ')
n3 = int(input())

if n1 > n2:
    medio = n1
    xtem = n2
else:
    medio = n2
    xtem = n1

if medio > n3:
    medio = n3

if medio < xtem:
    medio = xtem


print('El número intermedio es: ', medio)
