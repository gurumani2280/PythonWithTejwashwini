# create a function with keyword variable length argument --> **n

def func3(**n):
    print(type(n))    # <class 'dict'>
    print(n)
func3(name='test' , age='25',city='blre')     #{'name': 'test', 'age': '25', 'city': 'blre'}