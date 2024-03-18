#write a function to find the factorial of the given number

def factorial(n) :
    if n==0 or n ==1 :
        return 1
    else :
        return n * factorial(n-1)

n = int(input("please enter a number whose factorial needs to be calculated \n"))
factorial(n)
print("The factorial of ",n,"is",factorial(n))