#Creating Function
def f1():
    print("Called f1")

def f2(f):
    f()

f2(f1)

#Creating Wrapper Function
def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper

@f1
def f(a, b=9):
    print(a,b)

@f1
def add(x,y):
    return x + y

print(add(4,5))
