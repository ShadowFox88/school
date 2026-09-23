l = input()

l = [int(i) for i in l.split(" ")]

if len(l) % 2 == 0:
    average = (l[len(l) // 2] + l[(len(l) // 2) - 1]) // 2
else:
    average = l[len(l) // 2]

print(average)