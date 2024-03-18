#take one user input , and check whether it is between 0-100

a = int(input("enter any number\n"))
if a>0 and a<100:
    print(f"{a} is between 0-100")
else:
    print(f"{a} is not between 0-100")