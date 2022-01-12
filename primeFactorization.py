from math import sqrt, log, floor, pow


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if isPrime(i) and n % i == 0:
            return False
    return True


def primeFactorization(num, primes):
    primeFactors = {}
    for prime in primes:
        while True:
            if num % prime == 0:
                primeFactors[prime] = primeFactors.get(prime, 0) + 1
                num //= prime
            else:
                break
    return primeFactors


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if isPrime(n):
        print(n, "= 1 *", n)
    else:
        primes = []
        for i in range(2, n // 2 + 1):
            if isPrime(i):
                primes.append(i)
        primeFactors = primeFactorization(n, primes)
        noOfPrimes = len(primeFactors)
        print(n, "=", end=" ")
        for base, power in primeFactors.items():
            print(str(base) + "^" + str(power), end="")
            if noOfPrimes != 1:
                print(" * ", end="")
            noOfPrimes -= 1
        print("\nBase:Power Form: ", primeFactors, end="")
