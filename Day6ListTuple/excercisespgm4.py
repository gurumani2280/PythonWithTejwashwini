#print sum of all odd numbers from the list of numbers

a = [1,2,3,4,5]
#x = range(1,a+1,1)
addition = 0
for i in a :
    if i % 2 !=0 :
        #print(i,end=" ")
        addition = addition+i
    print("addition",addition)