from math import pi,sqrt,cos

x = 0.1
while (x <=2.5):
    y = sqrt(x)-2*cos(0.5*pi*x)
    x = round(x,2)
    print(x,"  ",y)
    x += 0.2
