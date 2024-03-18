#int conversion
# for boolean to int conv, TRUE int() will convert to 1 and for FALSE int() will convert to 0
x = True
print(int(x))

y = False
print(int(y))

print(int(7.9))
#float to int conv , this will only take the non-decimal part and will print the same

# str to int conv ,
# if  a string is containing only numbers (decimal should not be there) then it will convert to the respective number
z = "20"
print(int(z))

a = "20.5"
#print(int(a))  # ValueError: invalid literal for int() with base 10: '20.5'


b = "Test10"
#print(int(b))   #ValueError: invalid literal for int() with base 10: 'Test10'
