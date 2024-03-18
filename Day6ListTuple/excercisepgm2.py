#take a user input string and find out how many unique vowles are there
a = input("Please enter the string \n")
#vowel = 'aeiou'   # declaring as s string
vowel = ['a','e','i','o','u']
count = 0
for char in set(a):      # for taking unique values
    #print(char in vowel)
    #print(vowel.count(char))
    if vowel.count(char)>=1:
        count = count +1
        print(char," is a vowel ",count)
    else:
        print(char," is not a vowel")

print("count is ",count)
