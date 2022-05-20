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


# demonstrating the use of inheritance

class BCA(Student):
    def __init__(self, fname, lname, gender, age, progLang):
        super().__init__(fname, lname, gender, age)
        self.progLang = progLang
    def detail(self):
       return 'Name: {} {} \nGender: {}\nAge: {}\nprogLang: {}'.format(self.fname, self.lname, self.gender, self.age, self.progLang)


class BHM(Student):
    def __init__(self, fname, lname, gender, age, workArea):
        super().__init__(fname, lname, gender, age)
        self.workArea = workArea 
    def info(self):
       return 'Name: {} {} \nGender: {}\nAge: {}\nworkArea: {}'.format(self.fname, self.lname, self.gender, self.age, self.workArea)


s2 = BCA("Kabir", "Deula", "Male", 24, "Dart")
s3 = BHM("Jasmina", "Magar", "Female", 21, "House Keeping" )


print(s2.detail())
print(s3.info())


# method overridding

class University():
    def __init__(self):
        self.value = "Tribhuwan university"

    def display(self):
        print(self.value)

class College(University):
    def __init__(self):
        super().__init__()
        self.value = "NCCS"
    
    def display(self):
        return super().display()

obj1 = University()
obj2 = College()

obj1.display()
obj2.display()
        



