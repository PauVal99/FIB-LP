def my_map(f, L):
    return [f(l) for l in L]

def my_filter(f, L):
    return [l for l in L if f(l)]

def factors(n):
    return [x for x in range(1, n + 1) if n % x == 0]

def triplets(n):
    return [(a, b, c) for a in range(1, n + 1) for b in range(1, n + 1) for c in range(1, n + 1) if a*a + b*b == c*c]