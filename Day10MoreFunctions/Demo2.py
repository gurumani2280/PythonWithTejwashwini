#we can mix variable length with positional arguments

def func1(n1,*x) :
    print(n1)
    for i in x :
        print(i,end=",")
#print(func1())               #TypeError: func1() missing 1 required positional argument: 'n1'
print(func1(5))
func1(8,9,7,'hello')