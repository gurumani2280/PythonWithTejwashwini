#create a function which takes a number input and prints given input is even or odd

def even_odd(input):
    if input % 2 ==0 :
        print("the entered number is even")
    else :
        print("the entered number is odd")

input = int(input("Please enter a number \n "))
even_odd(input)