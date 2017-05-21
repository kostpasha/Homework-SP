a=float(input('Первое число: '))
b=float(input('Второе число: '))
c=float(input('Третье число: '))
if a<b:
  if a>c:
    print(a)
  elif b>c:
    print(c)
  else:
    print(b)
else:
  if a<c:
       print(a)
  elif b>c:
     print(b)
  else:
     print(c)