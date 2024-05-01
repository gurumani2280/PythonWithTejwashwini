file = open("myfile.txt","a")
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]

# i assigned ["This is Lagos \n","This is Python \n","This is Fcc \n"] to #variable L, you can use any letter or word of your choice.
# Variable are containers in which values can be stored.
# The \n is placed to indicate the end of the line.

file.write("Hello There \n")
file.writelines(L)
file.close()