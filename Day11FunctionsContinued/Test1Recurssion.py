# A function calling itself is called a recursive function
#advantages of recursive functions:
#1 can reduce code
#2 can solve complex problems using recursion by dividing a prob into a sub prob
# recursive func looks smaller simple and effective
#disadvantage:
#1 takes a lot of memory and time
#2 it is challenging to debug
#3 reasoning behind recursion can be difficult to think through easily

#question : print from n to 0

def recur1(n):
    print(n,end=", ")
    if n == 0:                 # this is termination condition for recursion
        return
    else:
        recur1(n-1)              # recursive call - reduced / changed n value
recur1(int(input("Please enter a number\n")))        # 6, 5, 4, 3, 2, 1, 0,


