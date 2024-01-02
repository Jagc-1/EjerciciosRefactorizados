#Muestra todos los números que estén en el rango de A y B


print("Número A: ")
A = int(input(":)"))
print("Número B: ")
B = int(input(":)"))

if A > B:
    for n in range(B, A):
        print(n + 1)
else:
    for n in range(A + 1, B):
        print(n)
