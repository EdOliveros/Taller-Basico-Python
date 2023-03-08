# 7. Escribir un programa que calcule el volumen de una esfera:
# Radio = 3 volumen de la esfera = 4/3 * PI * radio˄3

import math

rad = int(input("Cual es el radio de tu circunferencia?\n"))

def volumen(radio):

    p = math.pi

    print(f"radio: {radio}")
    print(f"pi: {p}")

    print(f"Volumen de la esfera => {(4/3) * p * (radio**3)}")


volumen(rad)