from functools import reduce

# lambda (anonymous function for single line functions)
a = lambda x, y: x + y
print(a(2, 4))

# filter (filters values of iterable based on return value of boolean function)
lst = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, lst)
print(evens)
print(list(evens))

# map (maps the values of iterable to the return value of the function)
mapped = map(lambda x: x ** 2, lst)
print(mapped)
print(list(mapped))

# reduce (reducing iterable into signle value) (a method from the 'reduce' module)
s = reduce(lambda x, y: x + y, lst)
print(s)
