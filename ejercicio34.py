#Calcula las ganancias de una Garita de Control, con cada vehículo que pasa.
import os
bus = 0
van = 0
micro = 0
man = 0
noc = 0

cantidad = int(input("Ingrese la cantidad de vehículos: "))

for cont in range(cantidad):
    os.system('cls')
    print("TIPO DE VEHICULO: ", cont+1, "/", cantidad, ": ")
    print("1. Ómnibus")
    print("2. Minivan")
    print("3. Micro")
    print("----------------------------------")
    tipo = int(input("Seleccione una opción: "))

    if tipo == 1:
        tarifa = 13
        bus += tarifa
    elif tipo == 2:
        tarifa = 10
        van += tarifa
    elif tipo == 3:
        tarifa = 8
        micro += tarifa

    turno = input("Turno (M/N): ").upper()
    if turno == "M":
        man += tarifa
    elif turno == "N":
        noc += tarifa
    os.system('pause')

print("----------------------------------------")
print("Ganancias de la mañana: ", man)
print("Ganancias de la noche: ", noc)
print("----------------------------------------")
print("Ganancias De Ómnibus: ", bus)
print("Ganancias De Minivan: ", van)
print("Ganancias De Micro: ", micro)
print("----------------------------------------")
