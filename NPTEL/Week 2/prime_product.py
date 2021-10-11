"""
A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .
Write a Python function isPrimeProduct(m) that takes an integer m as input and returns True if m is a prime product and
False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.
isPrimeProduct(6): True
isPrimeProduct(188): False
isPrimeProduct(202): True
"""

from math import sqrt
def isPrime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    sq_root = int(sqrt(n))
    for i in range(2, sq_root + 1):
        if isPrime(i) and n % i == 0:
            return False
    return True

def isPrimeProduct(n):
    if n < 0 or isPrime(n):
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0 and isPrime(i) and isPrime(n // i):
            return True
    return False

print(isPrimeProduct(188))
