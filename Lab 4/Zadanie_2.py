s = input("s: ")
r = ""
i = 0
while (i < len(s)-1):
    r += s[i+1]
    r += s[i]
    i += 2

print(r)
