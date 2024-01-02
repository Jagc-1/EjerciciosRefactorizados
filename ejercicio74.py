#Algoritmo que muestre si un número ingresado es capicúa

print('ingrese un numero de 3 cifras: ')
number = int(input())

c1 = (number - (number % 100))/100
r1 = number % 100
c2 = (r1 - (r1 % 10))/10
r2 = r1 % 10

if number == ((r2 * 100) + (c2 * 10) + c1):
    print(f'El numero {number} es capicúa')
else:
    print(f'El numero {number} no es capicúa')
