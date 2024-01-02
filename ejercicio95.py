#Algoritmo que muestre el nivel académico de un alumno según la nota ingresada.

print('Ingrese Nota 1: ')
nota1 = float(input(':)'))

print('Ingrese Nota 2: ')
nota2 = float(input(':)'))

print('Ingrese Nota 3: ')
nota3 = float(input(':)'))

prom = (nota1 + nota2 + nota3) / 3

if prom < 1.0:
    print('Nivel Malo')
elif prom > 1.0 and prom < 1.6:
    print('Nivel Regular')
elif prom > 1.6 and prom < 2.0:
    print('Nivel Bueno')
elif prom > 2.0:
    print('Nivel Excelente')
