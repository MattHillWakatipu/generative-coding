# Fibonacci numbers module

def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def fib_round2(n):  # write Fibonacci series up to n
    a, b = 0, 1
    count = 0
    while count < n:
        print(b, end=' ')
        a, b = b, a + b
        count += 1
    print()


def fib2_round2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    count = 0
    while count < n:
        result.append(b)
        a, b = b, a + b
        count += 1
    return result


def fib_round3(n):  # write Fibonacci series up to n
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
    print()


def fib2_round3(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    count = 0
    while count < n:
        result.append(a)
        a, b = b, a + b
        count += 1
    return result


if __name__ == "__main__":
    # fib(10)
    fib_round3(10)
