#ALGORITMO QUE MUESTRE EL COLOR MAS VOTADO
r = 0
v = 0
a = 0

print("Cantidad de Personas: ")
n = int(input(":)"))

for i in range(n):
    print("Persona Nro ",i,":")
    color = ''
    if (color != "rojo" and color != "verde" and color != "azul"):
        print("ROJO - VERDE - AZUL")
        color = str(input(":)"))
        print("----------------------")
        if color == "rojo":
            r += 1
        elif color == "verde":
            v += 1
        elif color == "azul":
            a += 1

    if (r > v and r > a):
        Mcolor = "ROJO"
    elif (v > r and v > a):
        Mcolor = "VERDE"
    else:
        Mcolor = "AZUL"
print("--------------------------------")
print("Cantidad de color Rojo: ", r)
print("Cantidad de color Verde: ", v)
print("Cantidad de color Azul: ", a)
print("El color mas votado es: ", Mcolor)
print("--------------------------------")
