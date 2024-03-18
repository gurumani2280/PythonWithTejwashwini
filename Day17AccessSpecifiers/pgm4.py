'''
create a class Chairs from the base class Furniture
Furniture will have default type of wood as Teak wood
User should have option to change type of wood
no of legs should be private (cannot be changed from outside)

'''

class Furniture :
    def __init__(self):
        self._typeofwood = 'Teak Wood'

class Chair(Furniture) :
    def __init__(self):
        super().__init__()
        self.__nooflegs = 4
    def displaychairinfo(self):
        print("This chair is made of {} and has {} legs".format(self._typeofwood,self.__nooflegs))
    def settypeofwood(self,typeofwood):
        self._typeofwood = typeofwood
chair1 = Chair()
chair1.displaychairinfo()
chair1.settypeofwood("Rose wood")
chair1.displaychairinfo()


