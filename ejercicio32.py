#Código que da regalos según el sexo y la edad del niño o niña.
import os

dayX = 29
monthX = 12
yearX = 2023
age = 0


for i in range(10):
    print("--------------------")
    dni = input("Ingrese su DNI: ")
    day = int(input("Ingrese día de nacimiento: "))
    month = int(input("Ingrese mes de nacimiento: "))
    year = int(input("Ingrese año de nacimiento: "))
    genre = input("Ingrese género (H/M): ").upper()
    print("---------------------")
    print("Fecha Actual: ", dayX, "/", monthX, "/", yearX)
    age = yearX - year

    if month > monthX or (month == monthX and day > dayX):
        age -= 1

    print(f"Tu edad es: {age} años")

    if age >= 8:
        print("Recibe Tablet.")
    elif age == 6:
        if genre == 'H':
            print("Recibe Carrito.")
        else:
            print("Recibe Muñeca.")
    os.system('pause')
    os.system('cls')
