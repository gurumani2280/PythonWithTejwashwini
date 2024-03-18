#create a function which takes two inputs and retuns both sum of difference of both the numbers

def sum_difference(x,y):    # here x and y are formal argumnents
    return x+y , x-y

print(sum_difference(2,3))  # (5, -1) # it is a tuple output , tuple has index
#here 2,3 are the actual arguments
a = sum_difference(5,7)  # this will be giving output as tuple
print("sum",a[0],"difference",a[1])   # hence here for printing we are calling the index values from the above output
#sum 12 difference -2

s,d =sum_difference(9,4)
print("sum" ,s,"difference",d)    #sum 13 difference 5



#notes:
#actual arguments in python is of 4 types:
#1.positional argumnets (This is the required ones) -if not given will get an error
#2. keyword argument (names=d argument as well) - passing the actual argumnets by using a keyword or the parameter names
# eg : print(sum_difference(2,3))
print(sum_difference(x=2,y=3))    #(5, -1)
print(sum_difference(y=2,x=3))    #(5, 1)

