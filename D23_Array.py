#Printing a buffer function using array which will ouput an address and size
from array import *

vals = array('i',[5,9,-8,4,2])

print(vals.buffer_info())

# #Printing a type of the code we are working with using 'typecode' function
from array import *

vals = array('i',[5,9,-8,4,2])

print(vals.typecode)

#Reversing a value in array using reverse function
from array import *

vals = array('i',[5,9,-8,4,2])
vals.reverse()

print(vals[0])

#Printing all values using for loops
from array import *

vals = array('i',[5,9,-8,4,2])

for i in range (5): 
    print(vals[i])
