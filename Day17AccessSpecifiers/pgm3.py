'''write program to create car rental system
1. display available cars and their rent per day
2. ask user input which car he wants to rent from the available cars
3. Ask user regarding the no of days the car is required for rent
4.Inform user regarding the rent amount'''

class CarRental :
    def __init__(self):
        self.carfaredict = {"swift":1000,"Tata":2000,"Hyundai":3000}
    def displayavailablecars (self):
        print("cost per day")
        for cars in self.carfaredict.keys():
            print(cars,"per day price",self.carfaredict[cars])
    def calcfare(self,car,noofdays):
        totalfare = self.carfaredict[car]*noofdays
        return totalfare

car1 = CarRental()
car1.displayavailablecars()
a = input("please enter the required car ")
b = int(input("please enter th no of days required"))
print("total fare for your requirement will be",car1.calcfare(a,b))

