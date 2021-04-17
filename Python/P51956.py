def myLength(L):
    length = 0
    for _ in L:
        length += 1
    return length

def myMaximum(L):
    max = L[0]
    for l in L:
        if l > max:
            max = l
    return max

def average(L):
    sum = 0
    for l in L:
        sum += l
    return sum / len(L)

def buildPalindrome(L):
    R = []
    for l in L:
        R.insert(0, l)
    return R + L

def remove(L1, L2):
    R = []
    for l in L1:
        if l not in L2:
            R.append(l)
    return R

def flatten(L):
    R = []
    for l in L:
        if isinstance(l, list):
            R += flatten(l)
        else:
            R.append(l)
    return R

def oddsNevens(L):
    O, E = [], []
    for l in L:
        if l % 2 == 0:
            E.append(l)
        else:
            O.append(l)
    return (O, E)

def primeDivisors(n):
    R = []
    for i in range(1, n + 1):
        if n % i == 0 and isPrime(i):
            R.append(i)
    return R

def isPrime(x):
    if x in [0, 1]:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True