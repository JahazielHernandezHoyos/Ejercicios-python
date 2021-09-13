# -*- coding: utf-8 -*-
"""

@author: jahaz
"""

print("Solo tienes 3 intentos")

contraseña1 = input("Escriba su contraseña: ")
limite = 3

contraseña2 = input("Escriba otra vez su contraseña: ")
contador = 1

while contraseña1 != contraseña2 and contador < limite:
        print("Las contraseñas no coinciden. Intentelo de nuevo.")
        contraseña2 = input("Escriba de nuevo su contraseña: ")
        contador += 1

if contraseña1 == contraseña2:
    print("Contraseña confirmada.")
else:
     print("La contraseña no se ha confirmado")