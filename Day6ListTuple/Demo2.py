x = [1,2,3,4,5,True,"Hello",7.98,4,5,2]
print(x)    # [1, 2, 3, 4, 5, True, 'Hello', 7.98, 4, 5, 2]
print(x[0])   #1
print(x[0:3])   # [1, 2, 3]
print(x.index(5))   #4
#print(x.index(7))     ValueError: 7 is not in list
print(x.index("Hello"))   #6
print(x.index(True))

print(x.count(4))   # it gives count of the number of times the value is present in the list  o/p - 2
