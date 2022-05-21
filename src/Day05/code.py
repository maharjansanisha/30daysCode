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

import math 
print(math.log(100))

import random
print(random.randrange(0, 10))  

import datetime
print(datetime.date.today())
print(datetime.datetime.now())

