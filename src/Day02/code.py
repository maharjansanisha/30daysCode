# Global Variables 

x = 'Hello' 
y = "World"

print("First: " + x + "\nSecond: " + y)

def hello():
    x = 'Hi'
    print("The world says: "+ x)

hello()
print("The world has to say: "+ x)

#Python numbers 

i = 7        #int
j = 7.5      #float
k = 5j       #complex (imaginary)
 
i, j, k = 7, 7.15, 5j
l = complex(k)
sum = float(i) + int(j)     # type casting

print(sum)
print(type(sum))
print(type(l))

# random numbers 

from dis import disco
from multiprocessing.connection import deliver_challenge
import random 
print(random.randrange(5, 25))

# format string 

num1 = 7
num2 = 21
string = "number{}, no.{}"
print(string.format(num1, num2))

# Python Boolean and Operators 

perPlate = 250
dis = 300
deliveryCharge = 100
noOfPlates = int(input("Number of plates: "))
totalCost = perPlate*noOfPlates

if(totalCost >= 1000):
    totalCost -= dis
else:
    totalCost += deliveryCharge

print("Your total cost is: Rs "+ format(totalCost))




