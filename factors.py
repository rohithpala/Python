from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if isPrime(i) and n % i == 0:
            return False
    return True


def factors(n):
    if isPrime(n):
        return [1, n]
    factor = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factor.append(i)
    factor.append(n)
    return factor


num = int(input("Enter Number: "))
print("Factors of " + str(num) + ": ", end="")
print(factors(num))
