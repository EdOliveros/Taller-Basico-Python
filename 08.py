# 8. Escribir un programa que calcule el área y el volumen de un cilindro:
# A = (2 * (PI * r˄2)) + ((2 * PI * r) * h)
# V = (PI * r2) * h

import math

rad = int(input("Cual es el radio de tu Cilindro?\n"))
alt = int(input("Cual es la altura de tu Cilindro?\n"))

def lonArea(radio, altura):

    p = math.pi

    print(f"radio: {radio}")
    print(f"pi: {p}")

    print(f"Area de la Cilindro => {(2 * (p * radio**2)) + ((2 * p * radio) * altura)}")
    print(f"Volumen de la Cilindro => {(p * radio*2) * altura}")


lonArea(rad, alt)