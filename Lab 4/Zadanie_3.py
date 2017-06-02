s1 = input('s1: ')
s2 = input('s2: ')
r = ''

for i in s1:
    if s2.find(i) != -1:
        r += i
print(r)
