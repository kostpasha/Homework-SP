import math
R1=float(input('Ввести значение R1: '))
R2=float(input('Ввести значение R2: '))
R3=float(input('Ввести значение R3: '))

v1=(4/3)*math.pi*R1**3
v2=(4/3)*math.pi*R2**3
v3=(4/3)*math.pi*R3**3

Z=(v1+v2+v3)/3

print('Значение v1: ', v1)
print('Значение v2: ', v2)
print('Значение v3: ', v3)
print()
print('Значение Z: ', Z)