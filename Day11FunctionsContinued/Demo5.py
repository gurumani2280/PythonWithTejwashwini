# Local and Global Variable

#a = 10       # global variable since it is declared outside a function and it can be used in all the functions

def func1():
    global a
    a = 9     # since the global variable's value is changes it takes the updated value.this is not a good practice

    print(a)

def func2():
    print(a)

func1()        #9
func2()        #9