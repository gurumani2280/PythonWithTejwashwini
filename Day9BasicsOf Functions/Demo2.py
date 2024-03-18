#create a function which takes one user argument as user name and prints a message along with the user name
def wish(name) :
    print("Hello",name,"How are you")
wish("Ishaan")
wish("Atharv")   # passing arguments

x = wish("test")
print("x",x)       #x None
#this prints none as we have not used the return statement