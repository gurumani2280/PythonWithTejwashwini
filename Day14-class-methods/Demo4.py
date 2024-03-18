# constructors is a spl method in pythin . its name will be __init__()
#when more than one constructor /methods are defined with same name and diff arguments , the latest ones will be executed
class Employee :
    weeklyWorkingHour = 40     # class variable
    weeklySalesMade = 5

    def __init__(self,name,sal,city):
        print("executing constructor")
        self.name = name
        self.sal = sal
        self.city = "Bangalore"

    def __init__(self,name,sal):        #self is the reference variable pointing to the current object
        print("executing constructor")  #whenever an obj is created constructor will be executed automatically
        self.name = name
        self.sal = sal

e1 = Employee("Test1",1000)            #TypeError: Employee.__init__() missing 2 required positional arguments: 'name' and 'sal'

e2 = Employee("Test2","2000")
e2.city = "Bangalore"
#print(e2.name)           #AttributeError: 'Employee' object has no attribute 'name'
print(e1.name)             #Test1
print(e1.sal)              #1000
print(e2.name)             #Test2
print(e2.sal)              #2000
print(e2.city)             #Bangalore