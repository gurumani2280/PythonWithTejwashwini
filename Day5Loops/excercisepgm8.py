#take user input n and print the n fibonacci numbers

n = int(input("Please enter the number of fibonacci numbers to be printed : \n"))
num1 = 0
num2 = 1
num3 = num1 + num2
count = 1
if n >= 1:
    print(num1,end=",")

if n >= 2:
    print(num2,end=",")

if n > 2 :
    count = 3
    while count <= n :
        print(num3 , end=",")
        count = count+1
        num1 = num2
        num2 = num3
        num3 = num1 + num2
print("\n The list is completed")
