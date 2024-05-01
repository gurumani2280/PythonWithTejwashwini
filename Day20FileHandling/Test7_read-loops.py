f = open("myfile.txt", "r")
for lines in f :
    print(lines)
f.close()

f = open("myfile.txt", "r")
for lines in f.readlines() :
    print(lines)
f.close()

