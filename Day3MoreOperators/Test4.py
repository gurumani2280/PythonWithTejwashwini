#indexing for string

g = "Hello World"
print(g[1])     #e
print(len(g))   #11
# len() gives the total character count including spaces starting from 0
print(g[9])    #l
print(g[10])   #d
#print(g[11])  IndexError: string index out of range

#negative indexes is allowed and it will be starting from the end i.,e from -1
print(g[-1])    #d
print(g[-11])   #H
#print(g[-13])   #IndexError: string index out of range

print('h' in g)   #False
print('W' in g)   #True
print('k' not in "Great")   #True