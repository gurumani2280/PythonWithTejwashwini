#how to remove elements from set

set1 = {4,5,6,7,'a','b','c'}
print(set1.pop())    #it removes the elements randomly 4
print(set1)      #{5, 6, 7, 'b', 'a', 'c'}

set1.remove(7)
print(set1)          # { 5, 6, 'c','a', 'b'}
#set1.remove(10)      #KeyError: 10
set1.discard(6)
print(set1)          #{4, 5, 'b', 'c'}

set1.discard(20)
print(set1)   # if element is not available discard method will not give any error {4, 5, 'c', 'a'}

if 7 in set1:
    set1.remove(7)

set1.clear()
print(set1)    #set() it will remove all the elements

#set1.pop()      # KeyError: 'pop from an empty set'   : pop on empty set will not work
#diff between pop , remove , discard , clear methods