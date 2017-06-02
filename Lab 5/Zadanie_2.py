arr = [int(s) for s in input("arr: ").split()]
s = 0

for i in arr:
    if (i < 0 and i % 2 == 0):
        s += i

for i in range(len(arr)):
    if (arr[i] % 3 == 0):
        arr[i] = s

print(arr)
