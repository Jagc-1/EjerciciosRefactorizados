#Dibuja un triángulo equilátero de números en secuencia
num = 0
val = 1
cont = 1


print("-----------------------------------------------")
print("-- MUESTRA GRÁFICA DE NÚMEROS COMO TRIÁNGULO --")
while num <= 0:
    num = int(input("Ingrese un número: "))

for x in range(num):
    espa = ' '
    for z in range(num - x - 1):
        espa += ' '
    print(espa, end='')

    for f in range(val):
        print(cont, end='')
        cont += 1
        if cont > 9:
            cont = 1
    cont = 1
    val += 2
    print()
