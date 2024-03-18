#3. Default Argument

def sum_difference(x,y=7):    # provided default value for variable y
    return x+y , x-y
print(sum_difference(2,y=3))     #(5, -1)  # comb of using positional and key word argument
#print(sum_difference(x=2,3))        #SyntaxError: positional argument follows keyword argument
print(sum_difference(8))   # (15, 1)
# we will be able to call the above function by providing one argument as well then the second arguments i.e., y will be a
#taken by default as '7'

print(sum_difference(y=9,x=8))
#print(sum_difference(y=9,8))   #SyntaxError: positional argument follows keyword argument

#after default argument , we should not take non default argument
#def test(x=5,y):   # SyntaxError: parameter without a default follows parameter with a default
 #   print(x,y)
#non default value should follow default parameter