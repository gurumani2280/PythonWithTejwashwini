set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print(set1.union(set2))   # both sets will be combined and duplicates will be avoided  #{70, 40, 10, 50, 20, 60, 30}
print(set1 | set2)     # this is another way of doing union

print(set1.intersection(set2))   # will find common in both sets
#or
print(set1 & set2)  # {40, 50, 30}

print(set1.difference(set2))
#or
print(set1 - set2)   # {10, 20}  # whatever elements is common in set2 is removed from set1

print(set1.symmetric_difference(set2))
#or
print(set1 ^ set2)    # {20, 70, 10, 60}  printing the unique elements

