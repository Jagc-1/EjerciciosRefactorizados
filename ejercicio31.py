#Algoritmo que ingrese un refrán y muestre el número de letras C, S, D, L, R y M que hay.

C = 0
S = 0
D = 0
L = 0
R = 0
M = 0
consonantes = 0


print("Ingresa un refrán: ")
refran = str(input(":)"))

for letra in refran:
    letra_mayuscula = letra.upper()

    if letra_mayuscula == 'C':
        C += 1
    elif letra_mayuscula == 'S':
        S += 1
    elif letra_mayuscula == 'D':
        D += 1
    elif letra_mayuscula == 'L':
        L += 1
    elif letra_mayuscula == 'R':
        R += 1
    elif letra_mayuscula == 'M':
        M += 1
    elif letra_mayuscula not in ['A', 'E', 'I', 'O', 'U']:
        consonantes += 1

print(f"Número de letras C: {C}")
print(f"Número de letras S: {S}")
print(f"Número de letras D: {D}")
print(f"Número de letras L: {L}")
print(f"Número de letras R: {R}")
print(f"Número de letras M: {M}")
print(f"Cantidad de consonantes: {consonantes}")
