# write a program to print each character of the string index wise

x = input("Please enter a String")
i = 0
for c in x :
    print(f"the character at index {i} is {c} ")
    i = i + 1
print("below is another way of doing the same pgm")
for j in range(0,len(x)):
    print(f"the character at index {j} is {x [j]}")
print("below using while loop")
k = 0
while k<len(x) :
    print(f"the character at index {k} is {x [k]}")
    k = k+1
