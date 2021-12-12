#Printing a String Datatype
name = 'Chadni'
name2 = 'Sanju'
print(name)
print(type(name))

print(name2)
print(type(name2))

#Slicing
name = 'Chadni'
print(name)

print(name[0])

#Skip Value
myStr = 'abcdefghijklmnopqrstuvwxyz'

print(myStr[2:6])
print(myStr[1:6:2])

#String Functions
myStr = 'abcdefghijklmnopqrstuvwxyz'

print(len(myStr))
print(myStr.endswith('abcd'))

print(myStr.startswith('xyz'))
print(myStr.count('ab'))

myStr = 'my name is chadni.'
print(myStr.capitalize())
print(myStr.find('name'))

print(myStr.replace('name','date'))

#Escape Sequences
myName = 'My Name\nis Chadni.'
print(myName)