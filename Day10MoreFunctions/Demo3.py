#we can mix variable length with positional arguments

def func2(*x,n1) :
    print(n1)
    for i in x :
        print(i,end=",")
#print(func2())               #TypeError: func2() missing 1 required keyword-only argument: 'n1'
#print(func2(5))               #TypeError: func2() missing 1 required keyword-only argument: 'n1'

func2(8,9,7,'hello',n1='world')


# note : after variable length argument if we are taking any other argument type then we should provide value as
# keyword argument

help(print)
#print(*args, sep=' ', end='\n', file=None, flush=False)