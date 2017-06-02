arr = [int(s) for s in input().split()]

result = []
i = 0
while (arr[i] != -1):
    if (arr[i] >= 3 and arr[i] <= 13):
        result.append(arr[i])
    i += 1

print(result)
