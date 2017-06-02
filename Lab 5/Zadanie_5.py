n = int(input("n: ")) 
a = [[int(j) for j in input("row: ").split()] for i in range(n)]

m = a[0][0]
m_i = 0

for i in range(len(a)):
    if (m > min(a[i])):
        m = min(a[i])
        m_i = i
r = []

for i in range(len(a)):
    r.append(a[i])
    if (i == m_i):
        r.append(a[0])

print(r)
