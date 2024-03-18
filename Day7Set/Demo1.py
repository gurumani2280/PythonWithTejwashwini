# creating a set
# we cannot put duplicates inside a set

a = { 1,2,3,"world",2,1}
print(a)             # {1, 2, 3, 'world'} -> it will not print teh duplicates and also the order might not be the same
print(type(a))    #<class 'set'>

#creating an empty set
b = {}
print(b)
print(type(b))   # <class 'dict'>

#right way of creating an empty set
c = set()
print(c)      # set()
print(type(c))     #<class 'set'>

# indexing and slicing will not work in set
print(a[1])   # TypeError: 'set' object is not subscriptable