#Inheritence : child class will inherit all the attributes and methods of the parent class

class Person :                                        #parent class
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def PrintPersonDetails(self):
        print(self.firstname,self.lastname,self.age)

P1 = Person("Tejaswini","Mohan",30)
P1.PrintPersonDetails()

class Student(Person) :                                        # child class inherting the parent class
    pass                                                       #use pass when you do not want to give any statement
S1 = Student("Ishaan","Atharv",2)
S1.PrintPersonDetails()

# in any blocks like if , func anywhere if we do noit want to type any statement but just we want a skeleton syntax then we can use "pass"
