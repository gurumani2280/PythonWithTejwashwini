# create a set and apply add and update methods
set1 = {3,4,5,6,3,4}
print(set1)      #{3, 4, 5, 6}
set1.add(10)     # it will add one element at a time
print(set1)      #{3, 4, 5, 6, 10}
set1.add(3)
print(set1)       #{3, 4, 5, 6, 10}   it will not add duplicate values

#set1.update(7)     ##TypeError: 'int' object is not iterable

set1.update("Hello")
print(set1)      # {'l', 'H', 'o', 3, 4, 5, 6, 10, 'e'}
# only list , tuple,range,another set and string can be updated and not int
# iterable only can be updated
#update will take one/multiple values

set1.update("Hello",range(5,8),[9,10],('z','x','f'),{'j','k','l'})
print(set1)       #{3, 4, 5, 6, 7, 'x', 'l', 10, 9, 'k', 'z', 'e', 'o', 'f', 'j', 'H'}

#Diff between add and update method




