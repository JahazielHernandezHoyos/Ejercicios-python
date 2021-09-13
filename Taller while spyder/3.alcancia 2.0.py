# -*- coding: utf-8 -*-
"""

@author: jahaz
"""

objetivo = int(input("¿cual es la meta de ahorros?: "))

print(objetivo)

ahorrado = 0 #contador

while objetivo > ahorrado:
    ingreso=int(input("¿Cuántos pesos quiere meter en la alcancia?: "))
    if ingreso <= 0:
        print (" no se permiten numeros menores a 0")
    else:
        ahorrado += ingreso

print(f"ahorrastes {ahorrado} pesos")