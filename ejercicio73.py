#Algoritmo que calcule el costo de una llamada telefónica


print('Cantidad de Minutos: ')
call = int(input(":)"))

if call < 5:
    costo = call * 0.9
else:
    costo = (5 * 0.9) + ((call - 5) * 1.1)

print('Costo de la llamada: $',costo)
