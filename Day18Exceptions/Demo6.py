print("before exception")
try:
    print(x)
except:
    print("some exception has occured")
except NameError as msg :
    print("name error has occured",msg)

else:
    print("else block-executes when exception doesn't occur")
finally:
    print("finally will execute everytime")
print("after exception")

'''File "C:\Users\Admin\PycharmProjects\PythonTesting\Day18Exceptions\Demo6.py", line 4
    except:
    ^^^^^^^
SyntaxError: default 'except:' must be last

Process finished with exit code 1'''