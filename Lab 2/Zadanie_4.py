g=float(input('Срок договора: '))
S=float(input('Сумма вклада: '))
if g==6:
    S=S*1.06
elif g==12:
    S=S*1.08
print (S)