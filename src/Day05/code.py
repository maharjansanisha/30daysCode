# Python Modules

# Creating and Calling a module

import mod as md

print(md.fac(7))


# Built in modules in Python

import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)

#Python Math

#Built-in Math function

x = min(7, 9, 26)       
y = max(87, 45, 34)

print(x)
print(y)

ab = abs(-453)  #returns the absoulte value of the given number
print(ab)

# Math Module

import math 
print(math.log(100))

import random
print(random.randrange(0, 10))  

#Python Date 
import datetime
print(datetime.date.today())
print(datetime.datetime.now())


x = datetime.datetime.now()

print(x.year)               #returns the year 
print(x.strftime("%A"))     #returns the name of the weekday

# creating a date object
x = datetime.date(2002, 8, 21)
print(x)
