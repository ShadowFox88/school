max_number = int(input("max num: "))
fizz_num = int(input("fizz num: "))
buzz_num = int(input("buzz num: "))

prime = [True for i in range(max_number + 1)]

p = 2
while (p * p <= max_number):
    if (prime[p]):
        for i in range(p * p, max_number + 1, p):
            prime[i] = False
    p += 1

for i in range(1, max_number + 1):
    if prime[i]:
        print("OOPS!")
    elif i % (fizz_num * buzz_num) == 0:
        print("FizzBuzz")
    elif i % fizz_num == 0:
        print("Fizz")
    elif i % buzz_num == 0:
        print("Buzz")
    else:
        print(i)