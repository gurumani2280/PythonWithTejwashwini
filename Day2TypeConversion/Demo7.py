# check whether given user input is even or odd

a = int(input("Please enter a number\n"))
# \n is used to move the cursor to next line
# \t is used to move cursor for next tab space
print(a)
if a%2 == 0:
    print(f"The given number {a} is even")
else:
    print(f"The given number {a} is odd")

    # f formatting is used to print a variable inside a string using {}
