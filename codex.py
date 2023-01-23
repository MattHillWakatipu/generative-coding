"""
Write me a python program which prints the first 10 Fibonacci numbers
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i))

print()
"""
Write me a python program which prints the first 10 Fibonacci numbers without using recursion
"""


def fibonacci_iterative(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci_iterative(10))
print()

"""
Write me a python program which prints the first 10 Fibonacci numbers iteratively
"""


def fibonacci_iterative_round2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


for i in range(10):
    print(fibonacci_iterative_round2(i))
