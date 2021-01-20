import os
import codecs
num = 0
directory_in_str = os.path.abspath(os.path.dirname(__file__)) + "\\" # Directory
directory_in_str.replace("c:", "C:") # The first letter is turned from c to C
directory =  os.fsencode(directory_in_str)
for file in os.listdir(directory): # For every file in the directory
    filename = os.fsdecode(file)
    f = codecs.open(directory_in_str + filename, "r", "UTF-8") 
    if filename.endswith(".js") or filename.endswith(".html'"): # If the file ends with cs
        if filename.endswith(".html") is False:
            for line in f:
                num += 1
        elif filename.endswith(".html"):
            num += len(f.readlines())
print(num)