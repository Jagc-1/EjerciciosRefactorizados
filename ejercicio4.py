#Muestra el nombre y el promedio del alumno con mejor nota en pseint
import os


for cont in range(5):
    print("-------------------")
    print("Nombre: ")
    nom = input(":)")
    print("Promedio: ")
    pro = float(input(":)"))
    if pro > xpro:
        xpro = pro
        xnom = nom
        os.system("cls")
os.system("pause")
print(f"Nombre: {xnom}")
print(f"Promedio: {xpro}")
