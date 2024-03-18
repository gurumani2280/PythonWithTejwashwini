#Lambda example to calculate square of a given number
a = lambda i : i**2
print(a (2))         #4
print(type(a))       #<class 'function'>

#lambda function to calculate cube of a given number
b = lambda j: j**3
print(b(3))      #27

#lambda function to find max of two given numbers
c = lambda x ,y : x if x > y else y
print(c(5,3))         #5

#lambda function to convert a given string to upper case using .uppermethod of a string
d = lambda str1 : str1.upper()
print(d('test'))          #TEST

