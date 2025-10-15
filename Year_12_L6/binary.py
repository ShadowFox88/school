import math
from useful import Chooser

def binary():
    n = int(input("Enter the number you wish to convert to binary: "))
    b = ""
    for i in range(0, int(math.log2(n)) + 1):
        if n % 2 == 1:
            b += "1"
        else:
            b += "0"
        
        n = n // 2
    
    return b[::-1].zfill(8)

c = Chooser()
c.add_choice(binary, "Convert Denary to Binary")

c.choose()