#take two user inputs x and y and print x to the power of y

def power(x,y):
    #x = int(input("please enter the value of x \n"))
    #y = int(input("please enter the value of x \n"))
    PowerOfx = (x**y)
    return PowerOfx
x = int(input("please enter the first value\n"))
y = int(input("please enter the second number\n"))
print(power(x,y))