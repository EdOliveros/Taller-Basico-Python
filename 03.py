# 3. Un programa que lea 4 números y calcule la media.
# Media= (num1 + num2 + num3 + num4)/4

num1 = int(input("N1 => "))
num2 = int(input("N2 => "))
num3 = int(input("N3 => "))
num4 = int(input("N4 => "))

def media(p1, p2, p3, p4):
    print(f"La media es\n{(p1 + p2 + p3 + p4)/4}")

media(num1, num2, num3, num4)