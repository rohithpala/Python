from math import sqrt, log, floor, pow


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if isPrime(i) and n % i == 0:
            return False
    return True


def primeFactorization(num):
    primeFactorizationResult = {}
    for prime in primes:
        if num % prime == 0:
            primeFactorizationResult[prime] = int(floor(log(num, prime)))
            num //= pow(prime, primeFactorizationResult[prime])  # Problem Here
    return primeFactorizationResult


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    primes = []
    for i in range(2, n // 2 + 1):
        if isPrime(i):
            primes.append(i)
    print(primeFactorization(n))
