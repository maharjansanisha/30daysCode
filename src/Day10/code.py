# Machine Learning
#Basics

import numpy 
# from scipy import stats 

arr = [34, 45, 76, 27, 53, 39, 45]
x1 = numpy.mean(arr)
x2 = numpy.median(arr)

x4 = numpy.std(arr)
x5 = numpy.percentile(arr, 50)
print(x1)
print(x2)

print(x4)
print(x5)

# a simple approach to find mode

y= [11, 8, 8, 3, 4, 4, 5, 6, 6, 6, 7, 8]

y.sort()
L1=[]

i = 0
while i < len(y) :
	L1.append(y.count(y[i]))
	i += 1

d1 = dict(zip(y, L1))


d2={k for (k,v) in d1.items() if v == max(L1) }

print("Mode:" + str(d2))

