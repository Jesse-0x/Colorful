from gmpy2 import *
import math
from binascii import hexlify
from gmpy2 import *
import math
import os
import sys
from tqdm import tqdm

def get_prime(state, bits):
    return next_prime(mpz_urandomb(state, bits) | (1 << (bits - 1)))

def get_smooth_prime(state, bits, smoothness=16):
    p = mpz(2)
    p_factors = [p]
    while p.bit_length() < bits - 2 * smoothness:
        factor = get_prime(state, smoothness)
        p_factors.append(factor)
        p *= factor

    bitcnt = (bits - p.bit_length()) // 2

    while True:
        prime1 = get_prime(state, bitcnt)
        prime2 = get_prime(state, bitcnt)
        tmpp = p * prime1 * prime2
        if tmpp.bit_length() < bits:
            bitcnt += 1
            continue
        if tmpp.bit_length() > bits:
            bitcnt -= 1
            continue
        if is_prime(tmpp + 1):
            p_factors.append(prime1)
            p_factors.append(prime2)
            p = tmpp + 1
            break

    p_factors.sort()

    return (p, p_factors)

e = 0x10001
SEED  = mpz(hexlify(os.urandom(32)).decode(), 16)
STATE = random_state(SEED)

def smooth(get):
    while True:
        p, p_factors = get_smooth_prime(STATE, get, 16)
        if len(p_factors) != len(set(p_factors)):
            continue
            # Smoothness should be different or some might encounter issues.
        q, q_factors = get_smooth_prime(STATE, get, 17)
        if len(q_factors) != len(set(q_factors)):
            continue
        factors = p_factors + q_factors
        if e not in factors:
            break
    return p, q
while True:
    p, q = smooth(int(input("bit lenght:")))
    print("P: " + str(int(p)))
    print("Q: " + str(int(q)))
    print("N: "  +  str(int((p * q))))