#set1 = frozenset(1,2,3,"hello")
#print(set1)
#print(type(set1))     #TypeError: frozenset expected at most 1 argument, got 4


set1 = frozenset("hello")   #cannot give multiple arguments which are iterable
print(set1)     #frozenset({'o', 'h', 'e', 'l'})
print(type(set1))    #<class 'frozenset'>

set2 = frozenset(range(3,8))
print(set2)    #frozenset({3, 4, 5, 6, 7})

set2 = frozenset([10])
print(set2)     #frozenset({10})

#frozenmethod is immutable form of set



