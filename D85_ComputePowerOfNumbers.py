# Python Program to Compute the Power of a Number

# Example 1: Calculate power of a number using a while loop
base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))
