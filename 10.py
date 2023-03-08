""" 10. Escribir un programa que calcule el volumen de un elipsoide
V = (4/3) * PI * a * b *c """

lado1 = int(input("Lado 1, => "))
lado2 = int(input("Lado 2, => "))
lado3 = int(input("Lado 3, => "))

import math
p = math.pi

def volumenElip(a, b, c):
    print(f"El volumen es: \n{(4/3) * p * a * b *c}")


volumenElip(lado1, lado2, lado3)