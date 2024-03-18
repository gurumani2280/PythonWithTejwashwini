#write a pgm to ask user input number till user wants . keep asking if he wants to add more numbers. print count of
#positive and negative numbers and zeroes entered by the user


def countofnumbers(n):
    countofpositive = 0
    countofnegative = 0
    countofzeroes = 0
    x = input("Do you want to enter a list of numbers (yes/no) ? \n ")
    if x == "yes":
        n = list("Please enter the list of numbers\n")
        for i in n :
            if i[k] == 0:
             countofzeroes = countofzeroes +1
             k = k+1
    elif i[k] > 0 :
        countofpositive = countofpositive + 1
        k = k+1
    elif i[k] < 0 :
        countofnegative = countofnegative + 1
        k=k +1
    else :
        break 

a = list(countofnumbers())
print(a)