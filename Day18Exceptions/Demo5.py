print("before exception")
try:
    print(x)
except NameError as msg :
    print("name error has occured",msg)
except:
    print("some exception has occured")
else:
    print("else block-executes when exception doesn't occur")
finally:
    print("finally will execute everytime")
print("after exception")

'''before exception
name error has occured name 'x' is not defined
finally will execute everytime
after exception

Process finished with exit code 0'''