#Algoritmo que muestra todos los números que son capicúa de tres cifras

c = 0
r = 0
c1 = 0
r1 = 0


for f in range(100, 1010):
    c = f // 100
    r = f % 10
    c1 = (f // 10) % 10
    r1 = r

    if f == ((r1 * 100) + (c1 * 10) + c):
        print(f, end=" ")
