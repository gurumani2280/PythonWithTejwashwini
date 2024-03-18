#using lambda func inside map()
#create a function which will give double of the input
def double(x):
    return 2*x
list1 = [4,2,3]
list2 = list(map(double ,list1))
print(list2)       #[8, 4, 6]

#using lambda
list3 = list(map(lambda x:2*x,list1))
print(list3)       #[8, 4, 6]

#square of each number in list using lambda and map
list4 = list(map(lambda x:x*x ,list1))
print(list4)       #[16, 4, 9]