# float conversion

# boolean to flaot : for TRUE float() will convert to 1.0 and for FALSE int() will convert to 0.0
x = True
print(float(x))

y = False
print(float(y))

print(float(7.9))


# for str to float conv : if  a string is containing only numbers (decimal can also not be there) then it will convert to the respective decimal ++number
z = "20"
print(float(z))

a = "20.5"
print(float(a))


b = "Test10"
print(float(b))   #ValueError: could not convert string to float: 'Test10'
