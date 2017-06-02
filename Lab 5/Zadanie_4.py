n = int(input("n: ")) 
a = [[int(j) for j in input("row: ").split()] for i in range(n)]

r = []

for i in a:
    r.append(max(i))

print(r)
