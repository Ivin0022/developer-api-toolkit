
gb = (i**2 for i in range(3))

def gen(n):
    for i in range(n):
        yield i

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b
