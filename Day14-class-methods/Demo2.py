# constructors is a spl method in pythin . its name will be __init__()

class Employee :
    weeklyWorkingHour = 40     # class variable
    weeklySalesMade = 5
    def __init__(self):        #self is the reference variable pointing to the current object
        print("executing constructor")  #whenever an obj is created constructor will be executed automatically
        self.name = "Test"
        self.sal = 3000
e1 = Employee()

e2 = Employee()
e2.city = "Bangalore"
#print(e2.name)           #AttributeError: 'Employee' object has no attribute 'name'
print(e1.name)             #Test1
print(e1.sal)              #1000
print(e2.name)             #Test2
print(e2.sal)              #2000
print(e2.city)             #Bangalore