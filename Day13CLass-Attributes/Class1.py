#class is a prototype/model/plamn/blueprint to create an object
# class provides a means of bundling data and functionalities together
#we can create a class to represent properties <attributes/variables> and actions<behaviour/methods> of an object
#class can contain both variables and methods

#how to define a class
class Test :
    '''This is just a dummy class'''      # doc string
    pass         #when we do not want to give any variables or methods we use pass

#how to create an object of a class:
obj1 = Test()     # syntax to create an obejct of a class
#in python everythings is object
print(obj1)           #<__main__.Test object at 0x000002ED2DF13650>
print(type(obj1))     #<class '__main__.Test'>
print(Test.__doc__)      #This is just a dummy class
print(Test.__dict__)    #{'__module__': '__main__', '__doc__': 'This is just a dummy class', '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>}
print(obj1.__dict__)    #{}->this is used to get attributes

#There are 2 types of variables:
#1 Class variable
#2 Instance Variable
# class variable : any variable created inside a class is known as class variable and class variable can be accessed
#using class name , using object also
#2 Instance Variable : this will be created usng reference variable or object or instance and this can be accessed using object only
