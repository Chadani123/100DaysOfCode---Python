#Using Break Statement
av = 5
x = int (input ("How many apples you have?"))

i = 1
while i<=x:

    if i>av:
        print("Out of Stock")
        break
    print("Apples")
    i+=1

print("Bye")

#Using Continue Statement
for i in range(1,101):

    if i%3 == 0:
        continue
    print(i)

print ("Bye")

#Using Pass Statement
for i in range (1, 101):

    if(i%2!=0):
        pass
    else:
        print(i)

print ("Bye")