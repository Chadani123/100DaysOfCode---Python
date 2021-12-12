# def greet ():
#     print ("Hello")
#     greet ()
# greet ()

'''
factorial(n) = n * factorial(n-1)
factorial(0) = 1 (By definition)
factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
'''

def factorial(n):
    #Base condition
    if(n ==0 or n==1):
        return 1
    return n* factorial(n-1)

a = factorial(7)
print(a)
