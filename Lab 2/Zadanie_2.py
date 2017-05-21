t=float(input('Время разговора: '))
dt=float(input('Продолжительность разговора: '))
s=float(input('Стоимость минуты разговора: '))
d=float(input('День недели от 1 до 7'))
st=1
if (d>5):
    if (t>22 and t<8):
        st=st*dt*s*0.3
    else:
        st=st*dt*s*0.2
else:
    if (t>22 and t<8):
        st=st*dt*s*0.2
    else:
        st=st*dt*s
print(st)
