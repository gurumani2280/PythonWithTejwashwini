#write a pgm to ask user input number till user wants . keep asking if he wants to add more numbers. print count and list of
#positive and negative numbers and zeroes entered by the user

CountOfZero = 0
CountOfPositive = 0
CountOfNegative = 0
while True :
    x = input("Do you want to enter a list of numbers (yes/no) ? \n")
    if x == "yes" :
        n = list((input("enter the list of numbers \n")))

        for i in n :

            if i[k] ==0 :
                CountOfZero = CountOfZero+1
                k = k+1
            elif i[k] > 0 :
                CountOfPositive = CountOfPositive +1
                k = k + 1
            elif i[k] < 0 :
                CountOfNegative = CountOfNegative +1
                k = k + 1
    else:
        break
print("count of Zeroes",CountOfZero)
print("count of Positive numbers",CountOfPositive)
print("count of Negative numbers",CountOfNegative)

