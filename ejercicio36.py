#Sumatoria de 4/2 – 9/1 + 15/1 – 23/2 + 34/8 – 49/64.
sumatoria = 0
v = 4
v1 = 5
v2 = 1
x = 2
x1 = 0.5
ope = "-"

print("-- Muestra Serie De Números --")
print("Valor de N: ")
n = int(input())

for i in range(n):
    if i != n:
        print(f"{v}/{x} {ope} ", end="")
    else:
        print(f"{v}/{x} {ope} ...")

    if i % 2 == 0:
        ope = "+"
        sumatoria = sumatoria + (v / x)
    else:
        ope = "-"
        sumatoria = sumatoria - (v / x)

    v = v + v1
    v1 = v1 + v2
    v2 = v2 + 1
    x = x * x1
    x1 = x1 + x1

print("\n---------------------------")
print("Sumatoria: ", sumatoria)
