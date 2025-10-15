import functools
import sys
import useful

sys.setrecursionlimit(99999)

@functools.cache
def fibonacci(n = None) -> int:
    if n is None:
        n = int(input("Enter number: "))
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_of_nth_fibonacci() -> int:
    n = int(input("Enter number: "))
    sum = 0
    for i in range(1, n):
        sum += fibonacci(i)

    return sum

useful.choose([useful.Choice(fibonacci, "Fibonacci nth term"), useful.Choice(sum_of_nth_fibonacci, "Sum of fibonacci till nth term")])