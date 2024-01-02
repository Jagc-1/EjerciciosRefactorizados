#Ingresar una frase y mostrar la cantidad de vocales que contiene.

a = 0
e = 0
i = 0
oo = 0
u = 0
vocal = ''


print("Ingresa una frase: ")
phrase = str(input(":)"))

for vocal in phrase:
    if vocal == 'A' or vocal == 'a':
        a += 1
    elif vocal == 'E' or vocal == 'e':
        e += 1
    elif vocal == 'I' or vocal == 'i':
        i += 1
    elif vocal == 'O' or vocal == 'Ó' or vocal == 'o':
        oo += 1
    elif vocal == 'U' or vocal == 'u':
        u += 1

print("-- CANTIDAD DE VOCALES --")
print("A: ", a)
print("E: ", e)
print("I: ", i)
print("O: ", oo)
print("U: ", u)
