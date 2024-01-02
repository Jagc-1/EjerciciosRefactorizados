# Pasar de números a letras


print('-- Pasar de números a letras --')
print('Ingrese un número de 2 cifras: ')
numero = int(input(':)'))

if numero > 0 and numero < 100:
    if numero > 10 and numero < 16:
        if numero == 11:
            print('ONCE')
        elif numero == 12:
            print('DOCE')
        elif numero == 13:
            print('TRECE')
        elif numero == 14:
            print('CATORCE')
        elif numero == 15:
            print('QUINCE')
    else:
        dec = (numero // 10)  # Obtener la decena
        uni = numero % 10  # Obtener la unidad

        if dec == 1:  # Obtener la decena
            decena = 'DIEZ'
        elif dec == 2:
            decena = 'VEINTE'
        elif dec == 3:
            decena = 'TREINTA'
        elif dec == 4:
            decena = 'CUARENTA'
        elif dec == 5:
            decena = 'CINCUENTA'
        elif dec == 6:
            decena = 'SESENTA'
        elif dec == 7:
            decena = 'SETENTA'
        elif dec == 8:
            decena = 'OCHENTA'
        elif dec == 9:
            decena = 'NOVENTA'

        if uni != 0:  # Obtener la unidad
            if uni == 1:
                unidad = 'UNO'
            elif uni == 2:
                unidad = 'DOS'
            elif uni == 3:
                unidad = 'TRES'
            elif uni == 4:
                unidad = 'CUATRO'
            elif uni == 5:
                unidad = 'CINCO'
            elif uni == 6:
                unidad = 'SEIS'
            elif uni == 7:
                unidad = 'SIETE'
            elif uni == 8:
                unidad = 'OCHO'
            elif uni == 9:
                unidad = 'NUEVE'

        if dec in [1, 2] and uni != 0 and not (numero > 10 and numero < 16):
            print(decena + unidad)
        else:
            print(decena + unidad)
else:
    print('El número ingresado no es válido')
