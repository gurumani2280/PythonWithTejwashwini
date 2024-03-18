#Inheritence : child class will inherit all the attributes and methods of the parent class

class Person :                                        #parent class
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def PrintPersonDetails(self):
        print(self.firstname,self.lastname,self.age)
    def IsStudent(self):
        return False

P1 = Person("Tejaswini","Mohan",30)
P1.PrintPersonDetails()
print(P1.firstname,"Is Student",P1.IsStudent())
class Student(Person) :                                        # child class inherting the parent class
    def IsStudent(self):
        return True                                        #changing the implementation in sub class as per the need of the sub class i.e., function overriding
S1 = Student("Ishaan","Atharv",2)
S1.PrintPersonDetails()
print(S1.firstname,"Is Student",S1.IsStudent())

# in any blocks like if , func anywhere if we do noit want to type any statement but just we want a skeleton syntax then we can use "pass"
