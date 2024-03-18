# Local and Global Variable

a = 10       # global variable since it is declared outside a function and it can be used in all the functions

def func1():
    a = 9
    print(a)             #9
    print(globals()['a'])    #10

def func2():
    print(a)              #10

func1()        #9
func2()        #9