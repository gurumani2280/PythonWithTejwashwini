# create a function with various kind of arguments

def func5(n1,n2,n3=4,n4=5):
    print(n1,n2,n3,n4)
#func5()                    #TypeError: func5() missing 2 required positional arguments: 'n1' and 'n2'
#func5(6,7,n2=8)     #TypeError: func5() got multiple values for argument 'n2'
func5(8,9)    # 8 9 4 5
func5(8,12,9)     # 8 12 9 5
func5(8,12,n4=9)      #8 12 4 9
