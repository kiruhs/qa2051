def prime_simple(n):
    # flag = False
    if n == 1:
        return False
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def fast_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
        # print(i)
    return True

def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [i for i in range(2, n + 1) if prime[i]]

