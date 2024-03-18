#Take numeric user input and display its respective alphabetical value in english

x = int(input("Please enter a number between 1-5\n"))
if x == 1 :
    print("ONE")
elif x == 2:
    print("TWO")
elif x == 3:
    print("THREE")
elif x ==4:
    print("FOUR")
elif x ==5:
    print("FIVE")
else:
    print(f"Given number {x} is out of range")
