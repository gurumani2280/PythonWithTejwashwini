x = [1,2,3]
print(len(x))   #3
x.append(4)   #   append() adds element to the end of the list
print(x)      # [1, 2, 3, 4]
x.insert(1,6)  # insert() adds element at the specified index
print(x)   # [1, 6, 2, 3, 4]
x.insert(0,0)
print(x)    # [0, 1, 6, 2, 3, 4]


x.insert(10,10)  # if given index value is more than the list index value then it will add the respective value to the end of the list
print(x)    # [0, 1, 6, 2, 3, 4, 10]


x.insert(-10,87)
print(x)    # [87, 0, 1, 6, 2, 3, 4, 10]

# difference b/w append() and insert()


