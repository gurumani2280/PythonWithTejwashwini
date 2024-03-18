class Animal :
    noOfLegs = 4
    @classmethod                     #classmethod is a decorator
    def walk(cls):                   #in class method , cls will be the argument using which we can access all the class variables
        print("no of legs",cls.noOfLegs)
Animal.walk()                         # instance is not created , its not required while using class method