import json
#person_str = '{"name": "Bob", "age": 12, "married": false, "children": null, "car": null, "student": true}'
person_str = '{"name": "Bob", "age": 42, "married": true, "children": ["sonu", "tonu"], "car": ["swift", "wagonR"], "student": false}'
person_dict = json.loads(person_str)
print(person_dict) # {'name': 'Bob', 'age': 42, 'married': True, 'children': ['sonu', 'tonu'], 'car': ['swift', 'wagonR'], 'student': False}
print(person_dict['married']) # True

number_list_str = '[1, 2, 3]'
print(type(json.loads(number_list_str))) # <class 'list'>
print(json.loads(number_list_str)) # [1, 2, 3]

number_str = '12.5'  #12 below line gives int <class 'int'>
print(type(json.loads(number_str))) # <class 'float'>
print(json.loads(number_str)) # 12.5

name_str = '"emexo"'  #  alone giving 'emexo' will throw error
print(json.loads(name_str)) # emexo
print(type(json.loads(name_str))) # <class 'str'>

bool1_str = 'true'
print(type(json.loads(bool1_str))) # <class 'bool'>
print(json.loads(bool1_str)) # True

bool2_str = 'false'
print(type(json.loads(bool2_str))) # <class 'bool'>
print(json.loads(bool2_str)) # False

null_str = 'null'
print(type(json.loads(null_str))) # <class 'NoneType'>
print(json.loads(null_str)) # None


