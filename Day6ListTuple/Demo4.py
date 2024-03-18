x = [1,2,3,4,5]
x.remove(2)    # give the value to remove from the list
print(x)    # [1, 3, 4, 5]

#x.remove(10)  # ValueError: list.remove(x): x not in list


x.pop()      # pop () removes the last element from the list
print(x)     #[1, 3, 4]

x.pop(1)     # removes the index(1) value
print(x)    # [1, 4]

#x.pop(10)      # IndexError: pop index out of range

x.clear()      # clear() removes all the elements of the list
print(x)

#difference b/w remove , pop and clear


