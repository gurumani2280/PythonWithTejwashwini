#write a pgm to find the frequency of each vowel present in a word
word = input("please enter a word \n")    # hello
d1 = {'a':0 , 'e':0 , 'i': 0 , 'o':0 , 'u':0}
for i in word.lower():
    if i in d1:
        value = d1[i]
        d1[i] = value +1
print("d1",d1)    #{'a': 0, 'e': 1, 'i': 0, 'o': 1, 'u': 0}
d1copy = d1.copy()    # because of runtimeerror we are copying the dict
for k in d1.keys() :        #RuntimeError: dictionary changed size during iteration
    if d1copy[k] == 0 :
        del d1copy[k]       #here we are removing an element which should not be done while iterating
print("d1copy",d1copy)    #{'e': 1, 'o': 1}

#if we do not want to get 0 values
d2 = {}
vowels = ['a','e','i','o','u']
for i in word.lower():
    if i in vowels:
        if i in d2:
            value = d2[i]
            d2[i] = value + 1
        else:
            d2[i] = 1
print("d2",d2)      # {'i': 1, 'a': 2}