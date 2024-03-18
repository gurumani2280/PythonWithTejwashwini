#take a user input list which have duplicate elements then remove duplicate from the list

word = (input("Please enter a word \n"))
print(word)
d1 = ""
for i in word :
    if i not in d1 :
        d1 = d1+i


print(d1)

#another way of doing the above pgm
print(str(set(word)))


