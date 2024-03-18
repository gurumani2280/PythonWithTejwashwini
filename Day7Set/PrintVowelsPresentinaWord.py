#ask user for one word , print the vowels present in the input word
word = input("please enter a word \n")    # hello
d1 = {'a':0 , 'e':0 , 'i': 0 , 'o':0 , 'u':0}
for i in word.lower():
    if i in d1:
        value = d1[i]
        d1[i] = value +1
print("d1",d1)



#another way :
s1 = set(word)
s2 = {'a','e','i','o','u'}
s3 = s1.intersection(s2)
print(s3)