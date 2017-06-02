x = int(input("x: "))
sum = 0

i = 1
rep = (x-1)/(x+1)
while (true):
    sum += (1/i)*rep**i
    i += 2

print(sum)
