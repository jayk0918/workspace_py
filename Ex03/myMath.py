pi = 3.14
def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def div(a, b):
    return a/b

def area_circle(r):
    return pi*r**2

print(__name__)

if __name__ == "__main__":
    print(plus(30, 10))
    print(minus(30, 10))
    print(multi(30, 10))
    print(div(30, 10))
    print(area_circle(4))