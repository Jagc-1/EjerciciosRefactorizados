#Algoritmo que muestre el área y volumen de un cilindro
pi = 3.1416

print("Ingrese el radio del cilindro: ")
r = float(input())
print("Ingrese la altura del cilindro: ")
h = float(input())

a = 2 * pi * r * (h  + r)
v =  pi * (r * r) * h

print("El área del cilindro es: ",a,"cm2")
print("El volumen del cilindro es: ",v,"cm3")
