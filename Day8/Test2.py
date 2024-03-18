y = {'a':'apple' , 'b':'banana' ,'p':'pineapple'}

#how to to remove values from dict

#del y['a']
#print(len(y))      #2
#print(y)     #{'b': 'banana', 'p': 'pineapple'}

#trying to remove the unavailable key
#del y['e']     #KeyError: 'e'

#y.pop('b')
#print(y)            #{'p': 'pineapple'}

#trying to remove the unavailable key
#y.pop('d')     #KeyError: 'd'

y = {'a':'apple' , 'b':'banana' ,'p':'pineapple'}
print(y.popitem())    # this will remove any element randomaly - ('p', 'pineapple')
print(y)    #{'a': 'apple', 'b': 'banana'}


#clear ()
y.clear()
print(y)      # it will remove all the values - {}
#y.popitem()      #KeyError: 'popitem(): dictionary is empty'
