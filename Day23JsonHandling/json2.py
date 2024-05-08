import json

person_dict = {'name': 'Bob', 'age': 12, 'married': False, 'children': None, 'car' : None, 'student':True}
with open(file='dict1.json', mode='w') as file1:
    json.dump(person_dict, file1)

number_list = [1, 2, 3]
with open(file='list1.json', mode='w') as file2:
    json.dump(number_list, file2)

number_tuple = (1, 5, 3)
with open(file='tuple1.json', mode='w') as file3:
    json.dump(number_tuple, file3)

number = 12
with open(file='number1.json', mode='w') as file4:
    json.dump(number, file4)

name = 'emexo'
with open(file='name1.json', mode='w') as file5:
    json.dump(name, file5)

bool1 = True
with open(file='bool1.json', mode='w') as file6:
    json.dump(bool1, file6)

bool2 = False
with open(file='bool2.json', mode='w') as file7:
    json.dump(bool2, file7)

none1 = None
with open(file='none1.json', mode='w') as file8:
    json.dump(none1, file8)

