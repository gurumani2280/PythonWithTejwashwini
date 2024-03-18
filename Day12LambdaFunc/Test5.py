#reduce() = will reduce to a single element and will give a single output

import functools
list1 = [2,5,6,8]
result = functools.reduce(lambda x,y:x+y,list1)      #NameError: name 'reduce' is not defined
print(result)        #21

result2 = functools.reduce(lambda x,y:x*y,list1)
print(result2)      #480