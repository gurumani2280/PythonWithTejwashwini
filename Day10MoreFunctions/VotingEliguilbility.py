#take age as user input and print if that user is eligible for voting or not

def eligibility(age):
    if age >=18:
        print("your are eligible to vote")
    else:
        print("you are not eligible to vote")
myage = int(input("Please enter your age\n"))
print(eligibility(myage))