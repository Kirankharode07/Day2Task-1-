# opening a file
file = open("example.txt", "r")
# reading from file
f = open("example.txt","r")
content= f.read()
line = f.readline()
lines = f.readlines()
f.close

# writing to a file
f= open("example.txt","w")
f.write("Hello World\n")
f.writelines(["Line1\n", "Line2\n"])
f.close()
# appending
f = open("example.txt","a")
f.write("Another line\n")
f.close()
# using with
with open ("example.txt", "r") as f:
    data = f.read()
    print(data)

# checking if file exists
import os
if os.path.exists("example.txt"):
    print("file exists")
else:
    print("No file")

# renaming or deleting a file
import os
os.remove("old.txt")
os.rename("old.txt","new.txt")