def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    result = 0
    for i in range(2, n):
        if is_prime(i):
            result += i
    return result

print(sum_of_primes(2000000))
