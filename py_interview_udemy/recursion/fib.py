# Given x, returns the x-th number in the fib sequence
def fib_rec(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib_rec(x - 1) + fib_rec(x -  2)

cache = [None] * 10

def fib_dyn(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        # Check the cache
        if cache[x] != None:
            return  cache[x]

        return fib_rec(x - 1) + fib_rec(x -  2)

print(fib_rec(1))
print(fib_rec(2))
print(fib_rec(3))
print(fib_rec(4))
print(fib_rec(5))
print(fib_rec(6))
print(fib_rec(7))

print(fib_dyn(8))