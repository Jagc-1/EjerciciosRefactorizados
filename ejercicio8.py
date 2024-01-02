# Muestra la serie gráfica de números 123456789 en forma decreciente

for f in range(10):
    serie = 0
    for c in range(10-f):
        serie = (serie * 10) + c
    print(serie)
