a=float(input('Введите число '))
b=float(input('Введите число '))
c=float(input('Введите число '))
if (((a<45 and b>=45 and c>=45)) or ((b<45 and a>=45 and c>=45)) or ((c<45 and a>=45 and b>=45))):
    print ('Completed')
else: print('Incompleted')