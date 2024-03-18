#create a function which takes an int parameter and returns square of the input
def square(num):
    print("inside square function with input",num)
    return num**2

#return is not mandatory but if we want to return some value then we can use return statement
square(2)
#return value of the above function we have not utilised in above line hence its not printing the value
print(square(3))
x = square(4)
print("x",x)
#whem we do not pass any arguments
#square()   # TypeError: square() missing 1 required positional argument: 'num'

print(square(num=3))