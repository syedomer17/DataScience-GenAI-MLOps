# file handling in python
# open a file
f = open("class22.py", "r")  # open file in read mode
# read the file
content = f.read()
print(content)
# close the file
f.close()

# reading a file using path 
file = open("/home/omar/syedomer17/README.md", "r")  # open file in read mode
content = file.read()
print(content)
file.close()

# for reading a file we need to write r in the open function and for writing a file we need to write w in the open function and for appending a file we need to write a in the open function
# writing to a file
f = open("class23.txt", "w")  # open file in write mode
f.write("This is a new file created using python")  # write to the file
f.close()  # close the file
# appending to a file
f = open("class23.txt", "a")  # open file in append mode
f.write("\nThis is an appended line")  # append to the file
f.close()  # close the file
# r a w x modes in file handling
# r - read mode (default)
# w - write mode (creates a new file or overwrites an existing file)
# a - append mode (creates a new file or appends to an existing file)
# x - exclusive creation mode (creates a new file, but raises an error if the file already exists)
# creqating a new file using x mode
try:
    f = open("class24.txt", "x")  # open file in exclusive creation mode
    f.write("This is a new file created using x mode")  # write to the file
    f.close()  # close the file
except Exception as err:
    print("File already exists")  # print this message if the file already exists

# with statement in file handling
# it is used to automatically close the file after the block of code is executed
with open("class25.txt", "r") as file:  # open file in read mode
    content = file.read()
    print(content)