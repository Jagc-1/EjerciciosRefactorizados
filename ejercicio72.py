#Programa que simule un login o clave de acceso
import os


print("-- Bienvenidos!! --")
os.system('pause')
os.system('cls')
username = str(input("Ingrese usuario: ")).upper()
password = int(input("Ingrese contraseña: "))
print('------------------------------------')

if username == 'ADMIN' and password == 123456:
    print("¡Accesso Permitido!")
else:
    print("¡Accesso Denegado")
