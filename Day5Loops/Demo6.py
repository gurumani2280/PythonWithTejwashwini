# Range function

# range syntax range(start index , end index ,step) end index will not be printed

x = range(0 , 10 ,1)
print(x)
print(type(x))
for i in x :
    print(i)
else:
    print("All the range items are printed")

a = list(x)    # converting range to list
print(a)
print(type(a))