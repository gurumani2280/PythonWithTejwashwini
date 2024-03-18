#find the frequency of letters in a given word

def frequency_of_letters(word):
    frequency = {}
    for letter in word :
        if letter in  frequency:
            frequency[letter]+=1
        else:
            frequency[letter]=1
    return frequency

word = input("Enter a word \n")
frequency = frequency_of_letters(word)
print("letter frequencies in the word", frequency)