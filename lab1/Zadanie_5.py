import math
x=float(input('Ввести значение: '))
a=-0.9
w=x**2*math.sqrt(math.fabs(a+x))
z=math.cos(a)**2+w**2
y=a*z**7+math.sin(w)**2
print('Значение a: ', a)
print('Значение y: ', y)
print('Значение z: ', z)
print('Значение w: ', w)