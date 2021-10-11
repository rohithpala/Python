from isPrime import isPrime
from math import log, floor, pow

def primeFactorization(num):
    primeFactorizationResult = {}
    for prime in primes:
        if num % prime == 0:
            primeFactorizationResult[prime] = int(floor(log(num, prime)))
            num //= pow(prime, primeFactorizationResult[prime]) # Problem Here
    return primeFactorizationResult

n = int(input("Enter a number: "))
primes = []
for i in range(2, n//2 + 1):
    if isPrime(i):
        primes.append(i)
print(primeFactorization(n))
