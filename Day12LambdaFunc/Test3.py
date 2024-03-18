#we can use lambda  commonly with filter() , map(),reduce(),
#create a function to filter out even number from the given list
a = [3,4,5,6,7,8]
def iseven(x):
    if x % 2 ==0:
        return True
    else:
        return False
a2 = list(filter(iseven,a))
print(a2)       #[4, 6, 8]


#same pgm with lambda function
a3 = list(filter(lambda x :x%2==0,a))
print(a3)       #[4, 6, 8]