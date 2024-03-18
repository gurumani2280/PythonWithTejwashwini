class Student :
    schoolname = "School1"
    uniform = "Blue dress"
    def __str__(self):
        print("printing the details ",self.name)
        print(self.schoolname)
        print(self.uniform)
        print(self.name)
        print(self.ID)
        print(self.standard)


obj1 = Student()
obj1.name = "Tej"
obj1.ID = "001"
obj1.standard = "std 5"

obj2 = Student()
obj2.name = "Ishaan"
obj2.ID = "002"
obj2.standard = "std 3"
# print("printing the details of obj1")
# print(obj1.schoolname)
# print(obj1.uniform)
# print(obj1.name)
# print(obj1.ID)
# print(obj1.standard)
#
# print("printing the details of obj2")
# print(obj2.schoolname)
# print(obj2.uniform)
# print(obj2.name)
# print(obj2.ID)
# print(obj2.standard)

obj1.__str__()
obj2.__str__()
# print(obj1)            #TypeError: __str__ returned non-string (type NoneType)
# print(obj2)