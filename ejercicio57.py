#ALGORITMO QUE MUESTRA LA CANTIDAD DE AÑOS, MESES Y DÍAS QUE HAY EN UNA FECHA INGRESADA.


days = int(input("Ingrese Cantidad de Días: "))

A = days // 365
M = (days % 365) // 30
D = (days % 365) % 30

print("Año:", A)
print("Mes:", M)
print("Día:", D)
