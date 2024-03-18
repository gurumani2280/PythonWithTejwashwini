#take two user input numbers and find the GCD of two numbers

a = int(input("Please enter the first number"))
b = int(input("Please enter the second number"))
if a == 0 :
    print("GCD is ",b)
elif b == 0 :
    print("GCD is ",a)
else:
    if a > b :
        min = b
    else :
        min = a
    for i in range(1,(min+1)) :
        if a % i == 0  and b % i ==0 :
            #print("printing i for debugging",i)
            GCD = i
    print("GCD final is",GCD)
#second type
import math
print("math.GCD",math.gcd(a,b))