n=int(input('Введите n: '))
Q=0
f=1
for k in range(1,n+1):
    f=f*k
    Q+=((k-3)**(k-5)*(k+7))/f
print (Q)
    
