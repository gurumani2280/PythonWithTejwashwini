#find the frequency of letters in a given word
word = input("Please enter a word \n")
d1 = {}
for i in word :
    if i in d1 :
        value = d1[i]
        d1[i] = value+1
    else:
        d1[i] = 1
print(d1)