d1 = {'a': 0, 'e': 1, 'i': 0, 'o': 1, 'u': 0}
keys = d1.keys()
for i in keys :        #RuntimeError: dictionary changed size during iteration
    if d1[i]==0 :
        d1.pop(i)
print(d1)