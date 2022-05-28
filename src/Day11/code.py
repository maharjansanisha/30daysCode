# Normal Data Distribution
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(0.5, 0.1, 5000)

plt.hist(x, 100)
plt.show()

# Scatter Plot

import matplotlib.pyplot as plt
studentId = [1, 2, 3, 4, 5, 6, 7]
marks = [45, 51, 32, 55, 47, 56, 30]
plt.scatter(studentId, marks)
plt.show()

# Linear Regression

import matplotlib.pyplot as plt

u = [3, 5, 6, 2, 8, 4, 2, 7, 5, 10, 11, 5]
v = [34, 43, 87, 53, 92, 34, 86, 77, 99, 111, 58, 69]

plt.scatter(u, v)
plt.show()

# Polynomial Regression

import matplotlib.pyplot as plt

stdId= [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
stdMarks = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(stdId, stdMarks)
plt.show()

# Compairing two data sets

import matplotlib.pyplot as plt

#arr_1
sID = numpy.array([1,2,3,4,5,6,7])
stdMarks = numpy.array([43, 43, 23, 57, 32, 51, 24])
plt.scatter(sID, stdMarks)

#arr_2
sID = numpy.array([1,2,3,4,5,6,7])
stdMarks = numpy.array([37, 45, 33, 55, 23, 23, 53])
plt.scatter(sID, stdMarks)

plt.show()

