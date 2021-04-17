def fibs():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a + b

def roots(x):
    yield x
    n = x
    while True:
        n = 0.5 * (n + (x / n))
        yield n

def isPrime(x):
    if x in [0, 1]:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

def primes():
    a = 2
    yield a
    while True:
        a += 1
        if isPrime(a):
            yield a

def isHamming(x):
    if x == 1:
        return True
    elif x % 2 == 0:
        return isHamming(x / 2)
    elif x % 3 == 0:
        return isHamming(x / 3)
    elif x % 5 == 0:
        return isHamming(x / 5)
    return False

def hammings():
    a = 1
    yield a
    while True:
        a += 1
        if isHamming(a):
            yield a
