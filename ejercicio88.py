#Algoritmo que muestre la estación del año al ingresar un número del 1 al 4.


print('-- Bienvenido, aqui sabras que estacion del año es --')
print('Ingrese número [1 - 4]: ')
numero = int(input())

if numero == 1:
    print('Es Primavera')
elif numero == 2:
    print('Es Verano')
elif numero == 3:
    print('Es Otono')
elif numero == 4:
    print('Es Invierno')
else:
    print('Error, dato no valido')
