#print sum of all odd numbers from 1 to n
n = int(input("enter the end number : "))
x = range(1,n+1,1)
#m = int(n)
addition = 0
for i in x:
    if i % 2 != 0:
        print(i, end=" ")
        addition = addition + i
print()
print("addition", addition)



