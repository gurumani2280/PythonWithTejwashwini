#write a pgm to ask user input number till user wants . keep asking if he wants to add more numbers. print count of positive and negative numbers and zeroes entered by the user

countOfZero = 0
countOfPositive = 0
countOfNegative = 0
while True :
    x = input("Do you want to enter a number (yes/no) \n")
    if x == "yes" :
        n = int(input("enter a number \n"))
        if n == 0:
            countOfZero = countOfZero + 1
        elif n>0 :
            countOfPositive = countOfPositive + 1
        elif n <0 :
            countOfNegative = countOfNegative + 1
    else:
        break
print("countOfZero",countOfZero)
print("countOfPositive",countOfPositive)
print("countofnegative",countOfNegative)