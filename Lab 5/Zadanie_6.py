n = int(input("n: ")) 
a = [[int(j) for j in input("row: ").split()] for i in range(n)]

for i in range(n):
    for j in range(n-i):
        x = n - i - 1
        y = n - j - 1
#        t = a[i][j]
#        a[i][j] = a[y][x]
#        a[x][y] = t
        a[i][j], a[x][y] = a[x][y], a[i][j]


for i in a:
    for j in i:
        print(j, end=" ")
    print()
