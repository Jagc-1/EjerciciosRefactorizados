#Algoritmo que muestre una cantidad de dinero en dólares y euros


print("-- Mostrar Dinero en Dolar y en Euro --")
dinero = float(input("Ingrese el monto de dinero: "))

dolar = dinero / 2.7
euro = dinero / 4

print("---------------------------------------------")
print("Cambio a Dolar: {:.2f}".format(dolar))
print("Cambio a Euro: {:.2f}".format(euro))
print("---------------------------------------------")
