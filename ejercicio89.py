#Algoritmo que muestre el nombre del mes, según el número ingresado del 1 al 12.


print('-- Bienvenido, aqui sabras que el mes es --')
print('Ingrese número [1 - 12]: ')
numero = int(input())

if numero == 1:
    print('Es Enero')
elif numero == 2:
    print('Es Febrero')
elif numero == 3:
    print('Es Marzo')
elif numero == 4:
    print('Es Abril')
elif numero == 5:
    print('Es Mayo')
elif numero == 6:
    print('Es Junio')
elif numero == 7:
    print('Es Julio')
elif numero == 8:
    print('Es Agosto')
elif numero == 9:
    print('Es Septiembre')
elif numero == 10:
    print('Es Octubre')
elif numero == 11:
    print('Es Noviembre')
elif numero == 12:
    print('Es Diciembre')
else:
    print('Opcion invalida, ingrese una opcion que si lo sea')
