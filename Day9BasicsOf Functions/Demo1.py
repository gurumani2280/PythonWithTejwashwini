#functions = group of python statements which will have a unique name and which we can call any number of times in
# our code
#function is designed for reusability so that code redundancy can be avoided
# two types of functions - built in functions and user defined functions
#user defined functions can be created using def()

# create a function to print "Hello" and call that function
#defining a function
def greeting() :
    '''This is doc string explaining the function'''
    # doc strings should be given immediately after the function definition

    print("hello")
    print("world")
    '''This is test'''   #this will not be printed
#calling the functions
greeting()
greeting()
print(greeting.__doc__)     # this will print whatever we have entered inside the triple quotes i.e., doc string
print(input.__doc__)
print(len.__doc__)
print(print.__doc__)