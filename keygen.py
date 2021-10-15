import random
from random import randint
import math
import large_prime_generator
from timeit import default_timer as timer

# ...

def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def isCoPrime(p, q):
    return gcd(p, q) == 1


def egcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def modInverse(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x


def dCalc(e, N):
    return modInverse(e, N)


def generateKeys(keysize=3):
    print("Generating Keys...")
    start = timer()

    # PRIME NUMBERS
    print("Generating Two Large Prime Numbers...")
    p = large_prime_generator.generate_prime_number()
    q = large_prime_generator.generate_prime_number()

    print(f"Prime number 1: {p}")
    print(f"Prime number 2: {q}")

    input("Press Enter to continue ...")

    # N
    print("Generating N...")
    N = p * q
    print(f"N: {N}")
    input("Press Enter to continue ...")

    # phiN
    print("Generating phiN...")
    phiN = (p - 1) * (q - 1)
    print(f"phiN: {phiN}")
    input("Press Enter to continue ...")
    
    # Generate Keys
    print("Generating e (ecnryption key)...")
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, phiN)):
            break
    print(f"e: {e}")
    input("Press Enter to continue ...")

    print("Generating d (decryption key)...")
    d = dCalc(e, phiN)
    print(f"d: {d}")
    print("All Keys Generated!")
    end = timer()
    print(f"Time Elapsed To Generate Key: {end - start} sec")
    return e, d, N
