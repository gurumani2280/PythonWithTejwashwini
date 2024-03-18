#example to find the max element from the list using lambda() and reduce()

import functools
x = [3,10,5,7,8]
print(x)
print("max element of the list is :",end=" ")
print(functools.reduce(lambda a,b: a if a>b else b,x))    #max element of the list is : 10
