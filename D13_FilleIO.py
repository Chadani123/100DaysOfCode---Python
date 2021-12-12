f = open("this.txt", "r")
text = f.read(6)
text = f.readline()
print(text)
text = f.readline()
print(text)
text = f.readline()
print(text)

textList = f.readlines()
print(textList)

f.close() 

f = open("write.txt", "w") #Write Mode
f = open("write.txt", "a") #Append Mode
f.write("This is just a test message.")
f.write("I want to write to this file.")
f.close()

#Using With Statement

with open("mine.txt", "w" ) as f:
    f.write("This file is mine.")