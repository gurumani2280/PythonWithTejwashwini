#string slicing
x = "Run Python"
a = x[1:3:1]     # syntax x[start index:end index:step]
print(a)

b = x[0:5:2]
print(b)

c = x[-1:-5]     #opposite index direction wont work for negative index values
print(c)

d = x[-1:-5:-1]     #if step value is not given it automatically takes it as 1
print(d)

e = x[:7]       #if start index is not given it will take 0 automatically
print(e)

f = x[2:]      #if end index value is not given then it will print till the end value
print(f)

g = x[-1:]
print(g)        # this prints only the last value

#reversing a string
h = x[::2]
print(h)     #start index is taken as 0 by default and end index will be taken as last index

i = x[::-1]    #start index is taken as -1 by default and end index will be taken as last index in the reverse direction
print(i)