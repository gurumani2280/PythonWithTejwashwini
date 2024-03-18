#create a dict using dict()
#another way of creating an empty dict
d1 = dict()
print(d1)    #{}
print(type(d1))      # <class 'dict'>

d2 = dict({1:'test' , 2:'demo',3:'excercises'})
#get() to access elements from the above dict
print(d2.get(1))      # test
print(d2.get(4))      #None

# keys() to access all the keys
print(d2.keys())   #dict_keys([1, 2, 3])

#values () to access all the values
print(d2.values())   #dict_values(['test', 'demo', 'excercises'])

#if we want to get all the keys and values
print(d2.items())     #dict_items([(1, 'test'), (2, 'demo'), (3, 'excercises')])

# To update a value to a dict
d2.update({4 : 'Testing', 5: 'Selenium'})
print(d2)          #{1: 'test', 2: 'demo', 3: 'excercises', 4: 'Testing', 5: 'Selenium'}

#indexing ,slicing is not there as order is not available in dict
d2.update({5 : 'cypress'})
print(d2)       #{1: 'test', 2: 'demo', 3: 'excercises', 4: 'Testing', 5: 'cypress'}