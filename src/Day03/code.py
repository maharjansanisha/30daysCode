# numeric pattern
import numbers

for i in range(0, 5):
    num = 1
    for j in range(0, i+1):
        print(num, end=" ")
        num = num + 1
    print()

# function ko find greatest among N numbers
arr = []
num = int(input('Enter N numbers: '))

for n in range(num):
    nums = int(input('Enter number %d:' % (n+1)))
    arr.append(nums)
print("Largest element among N numbers is: ", max(arr))

# program to find palindromes in a given list of string using Lamda
txt = ["racecar", "refer", "abc", "level", "Python"]
print("Orginal list of strings:")
print(txt) 
result = list(filter(lambda x: (x == "".join(reversed(x))), txt)) 
print("\nList of palindromes:")
print(result) 

#program to count number of uppercase and lowercase
txt = str(input("Enter a text:"))

l, u = 0, 0
for i in txt:
    if(i.isupper()):
        u += 1

    if(i.islower()):
        l+=1
     
print('Upper case characters: ',u)
print('Lower Case characters: ',l)


#program to find missing number in an array of numbers between 5-15
import array as arr
def test(num):
    return sum(range(5, 15)) - sum(list(num))

arrayNum = arr.array('i', [5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
print("Given array:")
for i in range(len(arrayNum)):    
    print(arrayNum[i], end=' ')
print("\nMissing number in array (5-15): ",test(arrayNum))
 
arrayNum = arr.array('i', [5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
print("\nGiven array:")
for i in range(len(arrayNum)):    
    print(arrayNum[i], end=' ')
print("\nMissing number in aray (5-15): ",test(arrayNum))