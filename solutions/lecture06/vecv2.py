def add(a, b):
    return op(a, b, lambda x, y: x + y)

def sub(a, b):
    return op(a, b, lambda x, y: x - y)

def mul(a, b):
    return op(a, b, lambda x, y: x * y)

def div(a, b):
    return op(a, b, lambda x, y: x / y)

def op(a, b, f):
    c = []
    for i in range(len(a)):
        c.append(f(a[i], b[i]))
    return c
