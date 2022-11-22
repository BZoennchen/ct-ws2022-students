def add(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

def sub(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] - b[i])
    return c

def mul(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

def div(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] / b[i])
    return c