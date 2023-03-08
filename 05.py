""" 5. Escribir un programa que calcule la longitud y el área de una circunferencia: 
Radio = 4
Longitud de la circunferencia = 2 * PI * radio
Área de la circunferencia = PI * radio˄2 
 """

import math

rad = int(input("Cual es el radio de tu circunferencia?\n"))

def lonArea(radio):

    p = math.pi

    print(f"radio: {radio}")
    print(f"pi: {p}")

    print(f"Longitud de la circunferencia => {2 * p * radio}")
    print(f"Area de la circunferencia => {p * (radio**2)}")


lonArea(rad)