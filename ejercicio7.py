#Muestra una serie gráfica de números del 9 al 1 en forma triangular

for f in range(10):
    s = 0
    serie = 0
    for c in range(9-f):
        s = 9-f
        serie = (serie * 10) + s
    print(serie)
