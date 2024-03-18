#Dictionary
#this is used for key value pair requirement and is mutable and keys cannot be dup;cate , it duplicate keys are assigned two values , existing value will be overrided with the new value
#creating an empty dictionary

x = {}
print(x)      # {}
print(type(x))      # <class 'dict'>

#add a new entry to the dict
x[1]='Test'
print(x)       #{1: 'Test'}

#use length () to get the length of the dict
print(len(x))     #1

# duplicate keys are not allowed , but duplicate values can be given
x[2] = 'Test'
print(x)     #{1: 'Test', 2: 'Test'}

#giving duplicate key and value , it will override the first given value
x[1] = 'demo'
print(x)    #{1: 'demo', 2: 'Test'}

#creating a dict with some values
y = {'a':'apple' , 'b':'banana' ,'p':'pineapple'}
print(len(y))     # 3
print(y)     #{'a': 'apple', 'b': 'banana', 'p': 'pineapple'}   <order can be different as well>
print(y['a'])   #apple

#if given key is not there
#print(y['c'])       #KeyError: 'c'
#print(y['cat'])       #KeyError: 'cat'

