# OOP in python

#Pclass and object
class Student:
    def __init__(self, fname, lname, gender, age):
        self.fname = fname
        self.lname = lname
        self.gender = gender 
        self.age = age 
        self.email = fname + '.' + lname + '@daumn.net'

    def bio(self):
        return 'Name: {} {} \nGender: {}\nAge: {}\nEmail: {}'.format(self.fname, self.lname, self.gender, self.age, self.email)

s1 = Student("Chandan", "Shakya", "Male", 23)

print(s1.email)
print(s1.bio())