#Enter 3 numbers from user and print there average

def average(a,b,c):
    avg = (a+b+c)/3
    return avg

x=int(input("Please enter the first number\n"))
y=int(input("Please enter the second number\n"))
z=int(input("Please enter the third number\n"))
print((average(x,y,z)))