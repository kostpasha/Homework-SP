from math import sqrt
x=float(input("Введите координату x "))
y=float(input("Введите координату у "))
if ((x<=1) and (y<=sqrt(x)) and (y>=-sqrt(x))):
    print("yes")
else:
    print("no")
