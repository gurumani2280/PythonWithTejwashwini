# Local and Global Variable

a = 10       # global variable since it is declared outside a function and it can be used in all the functions

def func1():
    a = 9   # a new local variable is created and if global and local both are there then local is given preference
    print(a)

def func2():
    print(a)

func1()
func2()