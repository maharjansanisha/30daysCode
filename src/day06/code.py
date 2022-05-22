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

#program to count total number of uppercase and lowercase and digits used in the txt file

f = open ("examp.txt", "a")
inp = input("Enter a text: ")
f.write(inp)
f.close()

def example():
    with open("examp.txt","r") as f1:
       data=f1.read()

    countUpper = 0
    countLower =  0
    countDigits = 0   

    for char in data:
        if char.islower():
            countLower+=1
        if char.isupper():
            countUpper+=1
        if char.isdigit():
            countDigits+=1
    print("Total Number of Upper Case letters are: ", countUpper)
    print("Total Number of Lower Case letters are :", countLower)
    print("Total Number of  digits are: ", countDigits)

example()