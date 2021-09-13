# -*- coding: utf-8 -*-
"""

@author: jahaz
"""


objetivo = float(input("¿cual es la meta de ahorros?: "))

ahorrado = 0 #contador

while objetivo > ahorrado:
    ahorrado += float(input("¿Cuántos pesos quiere meter en la alcancia?: "))

print(f"ahorrastes {ahorrado} pesos.")


