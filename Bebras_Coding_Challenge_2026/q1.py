n1 = int(input())
n2 = int(input())

total = 0

for i in range(n1, n2 + 1):
    if i % 3 == 0:
        total += i

print(total)