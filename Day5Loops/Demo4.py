# To get the sum of first n numbers
n = 20
x = 1
sum = 0
while x <=n :
    sum = sum+x
    x = x + 1
else :
    print("while loop is over",x)
print("sum",sum)  # use backspace to come out of the while loop
print("sum using formula",(n*(n+1))//2)