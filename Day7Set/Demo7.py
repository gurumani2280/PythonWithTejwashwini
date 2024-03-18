x = 10
#del x     # del is used to delete a variable
#print(x)    # NameError: name 'x' is not defined

a = "hello"
#del a[0]    # TypeError: 'str' object doesn't support item deletion / addition
#del a
#print(a)    # NameError: name 'a' is not defined

b = [1,2,3]
del b[0]
print(b)    # [2, 3]  index deletion is allowed in list
#del b
#print(b)     # NameError: name 'b' is not defined

c = (5,6,7)
#del c[0]      # TypeError: 'tuple' object doesn't support item deletion
#print(c)
del c
print(c)         # NameError: name 'c' is not defined