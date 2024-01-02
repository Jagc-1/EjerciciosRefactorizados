#Algoritmo que muestre el monto a pagar por una llamada telefónica según su destino


print('-- Bienvenido, aqui sabras el precio a pagar sehun el destino --')
print('1. Estados Unidos - $0.13')
print('2. Canadá - $0.11')
print('5. Ámerica del Sur - $0.52')
print('6. Ámerica Central - $0.99')
print('8. México - $0.17')
print('9. Europa - $0.17')
print('10. Asia - $0.20')
print('15. África - $0.59')
print('20. Oceanía - $0.28')
print('------------------------')

print('Seleccione un destino: ')
destino = int(input(':)'))
print('Duración de la llamada: ')
minutos = float(input(':)'))

if destino == 1:
    print('El costo $: ', minutos * 0.13)
elif destino ==  2:
    print('El costo $: ', minutos * 0.11)
elif destino ==  5:
    print('El costo $: ', minutos * 0.52)
elif destino ==  6:
    print('El costo $: ', minutos * 0.99)
elif destino ==  8:
    print('El costo $: ', minutos * 0.17)
elif destino ==  9:
    print('El costo $: ', minutos * 0.17)
elif destino ==  10:
    print('El costo $: ', minutos * 0.20)
elif destino ==  15:
    print('El costo $: ', minutos * 0.59)
elif destino ==  20:
    print('El costo $: ', minutos * 0.28)
else:
    print('Opcion invalida, ingrese una opcion que si lo sea')
