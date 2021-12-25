def factorial(n):
    return n * factorial(n-1)

num = int(input("Enter Number: "))
print(str(num) + "! = " + str(factorial(num)))
