# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0 , f"given {num} is not even"
except AssertionError as msg:
    print("Not an even number!",msg)
except:
    print("Not an even number!")

else:
    reciprocal = 1/num
    print(reciprocal)