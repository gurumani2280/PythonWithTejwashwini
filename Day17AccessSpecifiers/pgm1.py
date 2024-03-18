#Access Specifiers

class Person :
    def __init__(self,name,age,city):
        self.name = name
        self._age = age          # Protected attributes = can access from class and its sub class
        self.__city = city       #private attributes= can access only within the class
    def displaypersoninfo (self):
        print("person name",self.name,"person age",self._age,"person city",self.__city)

P1 = Person("Tejaswini","30","Mysore")
P1.displaypersoninfo()
print("person name",P1.name)
print("person age",P1._age)
#print("person city",P1.__city)        #AttributeError: 'Person' object has no attribute '__city'
print("person city",P1._Person__city)   #trying to access the private attribute outside the class using the "_"classname
