#Printing list using For Loops
list1 = [["Ram", 5],["Shyam", 8],["Hari", 12],["Sita", 14],["Gita", 16],["Rita", 18]]
 
dict1 = dict(list1)
print(dict1)
for item, mango in dict1.items():
    print (item, "and Mango is ", mango)

#Printing the numbers of list, greater than or equals to 6
items = [int, float, "Chadni", 5,3,3,22,10,14,3,4,233,100,500,2,1,0,5,3]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)