from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if isPrime(i) and n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter the Number to be Checked: "))
    if isPrime(num):
        print(str(num) + " is a prime number")
    else:
        print(str(num) + " is not a prime number")
