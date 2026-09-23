k = int(input())
s = input().strip()

l = []
m = []
temp = []

for i in range(0, len(s), k):
    l.append(s[i: i + k])

print(l)

if len(l[-1]) != 3:
    temp = l[-1]
    l[-1] = [] 

for i in l:
    s1 = ""
    for j in i:
        if j == "z":
            s1 += "a"
        else:
            s1 += chr(ord(j) + 1)
    
    m.append(s1)

m.append(temp)

print("".join(m))