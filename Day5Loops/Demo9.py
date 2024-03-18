# To display odd number from 0 to 20

x = range(0,20,1)
for i in x :
    if i%2 !=0 :
        print(i,end=",")
print("\n below is another way of doing the same pgm")
for j in range(1,20,2):
    print(j,end=" ")


