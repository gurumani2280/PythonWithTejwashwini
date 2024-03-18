#take tuple or set from teh user

x = eval(input("please enter a tuple in circular bracket\n"))      #(1,2,3,4)
print(x)      #(1,2,3,4,5)
print(type(x))    #<class 'tuple'>

x = eval(input("please enter a set in flower bracket\n"))       #{1, 2, 3, 4, 5}
print(x)      #{1, 2, 3, 4, 5}
print(type(x))    #<class 'set'>