#reduce() = will reduce to a single element and will give a single output

from functools import reduce
list1 = [2,5,6,8]
result = reduce(lambda x,y:x+y,list1)      #NameError: name 'reduce' is not defined
print(result)        #21

result2 = reduce(lambda x,y:x*y,list1)
print(result2)      #480


#difference b/w lambda and def
#1 lambda supports single line statements
#1 with def () we can create multiple statements
#2 lambda can sometimes reduce the readability of the code since we cannot use comments and doc string
#2 inside def doc string and comments will be allowed and will provide easy readability
#3 lambda func starts with lambda keyword and also known as anonymous function
#3 def function starts with def keyword and it will have a specific name of the function
