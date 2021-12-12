import os
working_dir = os.getcwd()
print(working_dir)

parent_dir = "/Users/chadaniacharya/Chand/Personal/100DaysOfCode/Python"
dir = "demo_dir"
new_dir = os.path.join(parent_dir, dir)
os.mkdir(new_dir)



