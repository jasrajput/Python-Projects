def fib(n):
    """printing a fibonacci sequence"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(20000)
