print("before exception")
try:
    print('x')
except:
    print("some exception has occured")
else:
    print("else block-executes when exception doesn't occur")
finally:
    print("finally will execute everytime")
print("after exception")

'''before exception
x
else block-executes when exception doesn't occur
finally will execute everytime
after exception'''