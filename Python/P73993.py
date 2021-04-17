from functools import reduce

def evens_product(L):
    return reduce(lambda acc, x: acc * x if x % 2 == 0 else acc, L, 1)

def reverse(L):
    return reduce(lambda acc, x: [x] + acc, L, [])

def zip_with(f, L1, L2):
    return [f(x, y) for x, y in zip(L1, L2)]

def count_if (f, L):
    return len([l for l in L if f(l)])