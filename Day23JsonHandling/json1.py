import json
person_dict = {'name': 'Bob', 'age': 12, 'married': False, 'children': None, 'car' : None, 'student':True}
#person_dict = {'name': 'Bob', 'age': 42, 'married': True, 'children': ['sonu','tonu'], 'car': ('swift', 'wagonR'),  'student':False}
person_json_str = json.dumps(person_dict)
print(person_json_str) # {"name": "Bob", "age": 12, "married": false, "children": null, "car": null, "student": true}
#{"name": "Bob", "age": 42, "married": true, "children": ["sonu", "tonu"], "car": ["swift", "wagonR"], "student": false}

number_list = [1, 2, 3]
number_list_str = json.dumps(number_list)
print(number_list_str) # [1, 2, 3]

number_tuple = (1, 5, 3)
number_tuple_str = json.dumps(number_tuple)
print(number_tuple_str) #[1, 5, 3]

number = 12
number_str = json.dumps(number)
print(number_str) # 12

name = 'emexo'
name_str = json.dumps(name)
print(name_str) # "emexo"

bool1 = True
bool1_str = json.dumps(bool1)
print(bool1_str)#true

bool2 = False
bool2_str = json.dumps(bool2)
print(bool2_str) #false

none1 = None
none1_str = json.dumps(none1)
print(none1_str) #null

