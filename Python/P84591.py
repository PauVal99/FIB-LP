def absValue(x):
    if x < 0:
        return -x
    return x

def power(x, p):
    r = 1
    for _ in range(p):
        r *= x
    return r

def isPrime(x):
    if x in [0, 1]:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

def slowFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slowFib(n-2) + slowFib(n-1)

def quickFib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
