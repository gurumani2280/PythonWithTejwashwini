#note : we can use both positional and key word arguments simultaneously but first we should use positional argument
#and then key word argument while calling a function otherwise an error will be shown

def sum_difference(x,y):    # here x and y are formal arguments
    return x+y , x-y
print(sum_difference(2,y=3))     #(5, -1)  # comb of using positional and key word argument
#print(sum_difference(x=2,3))        #SyntaxError: positional argument follows keyword argument
print(sum_difference(y=7,x=8))