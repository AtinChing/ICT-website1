import os
num = 0
directory_in_str = os.path.abspath(os.path.dirname(__file__)) # Directory
directory =  os.fsencode(directory_in_str)
print(directory_in_str)
print(directory)
for file in os.listdir(directory): # For every file in the directory
    filename = os.fsdecode(file)
    print(file)
    print(filename)
    f = open(directory_in_str + filename, "r") 
    if filename.endswith(".js") or filename.endswith(".html'"): # If the file ends with cs
        for line in f:
            num += 1
print(num)