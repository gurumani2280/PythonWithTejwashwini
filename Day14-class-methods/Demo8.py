class Person :
    age = 25

    #creating constructor:
    def __init__(self,name):
        self.name = name
    def printPersondetails(self):
        print("name {},age {}".format(self.name,self.age))

    @classmethod
    def printage(cls):
        print("person age is",cls.age)
        #print("person name",cls.name)          #inside class metjod we cannot access instance variables
Person.printage()              #person age is 25
P1=Person('Test')
P1.printPersondetails()

