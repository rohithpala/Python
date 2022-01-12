from functools import lru_cache
import time

start_time = time.time()
@lru_cache(None)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 201):
    print(fibonacci(i))

print("\n" + str(time.time() - start_time))