import time

start_time = time.time()

fibo_dict = {}
def fibo(n):
    if str(n) in fibo_dict:
        return fibo_dict[str(n)]
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibo(n - 1) + fibo(n - 2)
    fibo_dict[str(n)] = value
    return value

for i in range(1, 201):
    print(fibo(i))

print("\n" + str(time.time() - start_time))