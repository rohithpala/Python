import math

def factors(n):
    if isPrime(n):
        return [1, n]
    factor = []
    for i in range(1, n//2+1):
        if n%i == 0:
            factor.append(i)
    factor.append(n)
    return factor

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if isPrime(i) and n%i == 0:
            return False
    return True

def numberAsProduct(n):
    if(isinstance(math.sqrt(n), int)):
        return [math.sqrt(n), math.sqrt(n)]
    for i in range(n//2, 1, -1):
        if n%i == 0:
            return [i, n//i]

def f(n):
    if n == 1:
        return 0
    elif isPrime(n):
        return 1
    x,y = numberAsProduct(n)
    return x*f(y)+y*f(x)

def sumOfFofn(n):
    if n == 1:
        return 0
    elif isPrime(n):
        return 1
    l = factors(n)
    sum = 0
    for i in l:
        sum += f(i)
    return sum

def strange_sum (L, R):
    sum = 0
    for i in range(L, R+1):
        sum += sumOfFofn(i)
    return sum%998244353

T = int(input())
for _ in range(T):
    L, R = map(int, input().split())

    out_ = strange_sum(L, R)
    print (out_)
