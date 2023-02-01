# Example 2: Calculate power of a number using a for loop
base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))