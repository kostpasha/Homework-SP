s = input("s: ")
a = int(s,2)
t = ""
for i in range(len(s)):
    p = (i+2)%len(s)
    t += s[p]
b = int(t,2)

r = a - b
print(r)
