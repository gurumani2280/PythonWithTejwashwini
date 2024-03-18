# Local and Global Variable

def func1():
    a = 7   # local variable since it is declared inside a function and this cannot be accessed outside this function
    print(a)

def func2():
    print(a)      #NameError: name 'a' is not defined

func1()
func2()