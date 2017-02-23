'''
ProjectEuler#46
auther: Rohit Maurya
'''

# Solved using https://zach.se/project-euler-solutions/46/
from itertools import product
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
 
def prime_list(n):
    L = []
    for n in range(1, n):
        if isprime(n):
            L.append(n)
    return L


def main():
    primes = prime_list(10000)
    composites = set(n for n in range(2,10000) if n not in primes)
    twicesquares = set(2*(n**2) for n in range(100))

    sums = set(sum(c) for c in product(primes, twicesquares))
    print(min(n for n in composites if n not in sums and n % 2 != 0))

if __name__ == "__main__":
    main()
