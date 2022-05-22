# python file halndling

#creating a file in python
from asyncore import write

f = open("txt.txt", "w")

#writing to an existing file
f.write("File handling in Python.")
f.close()

s = open("txt.txt", "r")
print(s.read())
s.close()

#deleting a file
import os 
os.remove("txt.txt")