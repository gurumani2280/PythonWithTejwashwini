set1 = set("Hello")
print(set1)      # {'o', 'e', 'H', 'l'}
set2 = set(range(5))
print(set2)       #{0, 1, 2, 3, 4}
set3 = set([1,2,3,2,3,"hello"])
print(set3)    #{1, 2, 3, 'hello'}

set4 = set2.copy()
print(set4)       # {0, 1, 2, 3, 4}

