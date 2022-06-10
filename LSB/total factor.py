import math
import random
import time
from gmpy2 import *
from tqdm import tqdm


def _primes_yield_gmpy(n):
    p = i = 1
    while i <= n:
        p = next_prime(p)
        yield p
        i += 1


def primes(n):
    return list(_primes_yield_gmpy(n))


def pollard_P_1(n):
    """Pollard P1 implementation"""
    z = []
    logn = math.log(int(isqrt(n)))
    prime = primes(100000)

    for j in range(0, len(prime)):
        primej = prime[j]
        logp = math.log(primej)
        for i in range(1, int(logn / logp) + 1):
            z.append(primej)

    try:
        for pp in tqdm(prime):
            i = 0
            x = pp
            while 1:
                x = powmod(x, z[i], n)
                i = i + 1
                y = gcd(n, x - 1)
                print(i, x, y)
                if y != 1:
                    p = y
                    q = n // y
                    return int(p), int(q)
    except IndexError:
        return "a", n


def get_M(N):
    bound = round(int(math.pow(N, 1 / 6)))
    lt, prime, M = [], 1, 1
    while (prime <= bound):
        prime = int(next_prime(prime))
        lt.append(prime)
        M *= prime
        print(M, lt)
    return M


def b_get_M(N):
    lt, prime, M = [], 1, 1
    while (len(lt) <= N):
        prime = int(next_prime(prime))
        lt.append(prime)
        M *= prime
        print(M, lt)
    return M


def run(N):
    a = 2
    B = 1
    M = b_get_M(B)
    p = gcd(pow(a, M) - 1, N)
    while not (1 < p < N):
        B += 1
        M = b_get_M(B)
        p = gcd((a ** M) - 1, N)
        print(p, a, M)
    return p


if __name__ == '__main__':
    N = int(input("int N:"))
    start = time.time()
    p_l = []
    q_l = []
    p, q = pollard_P_1(N)
    while (q != 1 ) & ( (q not in q_l) | (p not in p_l)) &(p != "a"):
        p_l.append(p)
        q_l.append(q)
        p, q = pollard_P_1(q)
    end = time.time() - start
    print(f" P: {p_l} \n Q: {q_l} \n N: {N}")
    print("spend time: " + str(round(end, 4)))
