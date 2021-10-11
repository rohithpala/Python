def f(coefficients, x):
    l = len(coefficients)
    fx = 0
    for i in range(l - 1, -1, -1):
        fx += coefficients[i] * (x ** i)
    return fx


def rootUsingBM(coefficients):
    i = 0
    a : int
    b : int
    while True:
        fi = f(coefficients, i)
        fi1 = f(coefficients, i + 1)
        if (fi > 0 and fi1 < 0) or (fi < 0 and fi1 > 0):
            a = i
            b = i + 1
            break

    values = []
    while True:
        x = (a + b) / 2
        fa = f(coefficients, a)
        fb = f(coefficients, b)
        if (fa > 0 and fb < 0) or (fa < 0 and fb > 0):


degree = int(input("Degree of the Polynomial: "))
coefficients = [0] * (degree + 1)
for i in range(degree, -1, -1):
    if i == 0:
        coefficients[i] = int(input("Constant: "))
    else:
        coefficients[i] = int(input("Coefficient of x" + str(i) + ": "))
rootUsingBM(coefficients)
