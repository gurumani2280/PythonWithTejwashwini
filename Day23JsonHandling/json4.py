import json

with open(file='dict1.json', mode='r') as file1:
    dict1=json.load(file1)
print("python dict from json file ", dict1)

with open(file='list1.json', mode='r') as file2:
    list1 = json.load(file2)
print("python list1 from json file ", list1)

with open(file='tuple1.json', mode='r') as file3:
    tuple1 = json.load(file3)
print("python tuple1 from json file ", tuple1)

with open(file='number1.json', mode='r') as file4:
    number = json.load(file4)
print("python number from json file ", number)

with open(file='name1.json', mode='r') as file5:
    name = json.load(file5)
print("python name from json file ", name)

bool1 = True
with open(file='bool1.json', mode='r') as file6:
    bool1 = json.load(file6)
print("python bool1 from json file ", bool1)

with open(file='bool2.json', mode='r') as file7:
    bool2 = json.load(file7)
print("python bool2 from json file ", bool2)

with open(file='none1.json', mode='r') as file8:
    none1 = json.load(file8)
print("python none from json file ", none1)
