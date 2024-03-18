#factorial using Recursion

def fact(n):
    if n == 0 :
        return 1
    else:
        return n * fact(n-1)
x = int(input("Please enter a number\n"))
if x < 0:
    print("Please enter a valid positive number")
else:
    print(fact(x))



