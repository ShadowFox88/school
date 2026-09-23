signal = input().split(" ")

def encrypt(signal):
    counter = []
    last_value = ""

    for i in signal:
        if i == last_value:
            counter[-1][1] += 1
        else:
            counter.append([i, 1])
            last_value = i
    
    output = ""

    for i in counter:
        output += f"{i[0]} {i[1]} "

    return output

print(encrypt(signal))