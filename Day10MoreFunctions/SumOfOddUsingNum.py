#print sum of all odd numbers from 1 to n

def sumofodd(sum):

    x=range(1,n+1,1)
    sum = 0
    for i in x:
        if i % 2 !=0:
            print(i,end=", ")
            sum= sum + i
        print("sum of all odd numbers is",sum)
        return sum
n= int(input("please enter the end number\n"))
print(sumofodd(n))