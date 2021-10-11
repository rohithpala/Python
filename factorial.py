def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

num = int(input("Enter Number: "))
print(str(num) + "! = " + str(factorial(num)))
