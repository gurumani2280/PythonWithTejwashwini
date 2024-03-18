#lambda function is a small anonymous function ,we do not use def keyword and we can create a function with only a single line
#syntax lambda argument list : expression
# eg : Print hello

x = lambda : print("hello")
x()          # hello

#lambda example to print hello along with a given name
y = lambda name : print("hello",name)
y("Test")         # hello Test
y("Ishaan")       # hello Ishaan

#lambda example to add two numbers
z = lambda a,b :a+b    # no need of using return keyword
print(z(2,3))      #5
