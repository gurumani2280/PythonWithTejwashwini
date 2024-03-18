# Class Employee

class Employee :
    weeklyWorkingHour = 40     # class variable
    weeklySalesMade = 5
e1 = Employee()
e1.name = "Test1"          #instance variable
e1.sal = 1000
e2 = Employee()
e2.name = "Test2"
e2.sal = 2000
e2.city = "Bangalore"
#print(e2.name)           #AttributeError: 'Employee' object has no attribute 'name'
print(e1.name)             #Test1
print(e1.sal)              #1000
print(e2.name)             #Test2
print(e2.sal)              #2000
print(e2.city)             #Bangalore