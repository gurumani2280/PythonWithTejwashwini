#fibonacci series using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
x = int(input("Please enter a number\n"))
if x < 0:
    print("Please enter a valid positive value\n")
else:
    print("Fibonacci series till to n :",x)
    for i in range(x):
        print(fibonacci(i),end=", ")

