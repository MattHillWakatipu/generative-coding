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


def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_series_recursive(n):
    result = []
    for i in range(n):
        result.append(fib_recursive(i))
    return result


if __name__ == "__main__":
    print(fib_series_recursive(10))
