# Python Program to Return Multiple Values From a Function
# Example 1: Return values using comma
def name():
    return "John","Armin"

# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2 = name()
print(name_1, name_2)
