# constructors is a spl method in pythin . its name will be __init__()
#when more than one constructor /methods are defined with same name and diff arguments , the latest ones will be executed
class Employee :
    weeklyWorkingHour = 40     # class variable
    weeklySalesMade = 5


    def __init__(self,name,sal,city):
        print("executing constructor")
        self.name = name
        self.sal = sal
        self.city = city
    def displayEmpInfo(self):      # this is a instance method , we can call using the reference variable
        print('employee name {},salary {}, city {} , working hours {}, sales made {}'.format(self.name,self.sal,self.city,self.weeklyWorkingHour,self.weeklySalesMade))


e1 = Employee("Test1",1000,"goa")
e1.displayEmpInfo()

e2 = Employee("Test2","2000","ooty")
e2.displayEmpInfo()
