def fib_n(n, a = 0, b = 1):
    if n == 0:
        return a

    return fib_n(n-1, b, a+b)


print(fib_n(5))
print(fib_n(9))
print(fib_n(10))