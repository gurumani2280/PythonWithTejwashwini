#variable length argument  - * name of the variablename

#create a program to add variable number of input numbers

def sum(*n):
    print(len(n))
   # print(type(n))    # <class 'tuple'>
    total = 0
    for i in n :
        total = total + i
    return total
print(sum())
print(sum(2))
print(sum(3,4))
print(sum(3,4,6,7,7))

