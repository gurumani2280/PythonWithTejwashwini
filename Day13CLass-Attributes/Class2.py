#Create another class "student"

class Student :
    '''This is a student class'''
    schoolname = "VVVS"      # this is a class attribute/variable-common to all the objects of this particular 'student' class
print(Student.schoolname)    #VVVS
mohan = Student()            #creating object/instance of class Student
print(mohan.schoolname)      #VVVS
#print(Student.__dict__)      #{'__module__': '__main__', '__doc__': 'This is a student class', 'schoolname': 'VVVS', '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>}
#print(mohan.__dict__)        #{} -> its empty because we have not created any instance variables still

Student.dress = "Blue Uniform"  # creating a new class variable. this way is discouraged
print(Student.dress)         #Blue Uniform
print(mohan.dress)           #Blue Uniform
#print(Student.__dict__)      #{.........., 'schoolname': 'VVVS', ........., 'dress': 'Blue Uniform'}
#print(mohan.__dict__)        #{}
mohan.dress = "Red Uniform"  #new instance attribute is getting created having the same name as class attribute.
print(Student.dress)         #Blue Uniform - thsi will always tale class attribute value
print(mohan.dress)           #Red Uniform - printing the instance variable over class variable
#print(Student.__dict__)      #{.........., 'schoolname': 'VVVS', ........., 'dress': 'Blue Uniform'}
#print(mohan.__dict__)        #{'dress': 'Red Uniform'}
mohan.dress = "Green Uniform"
print(mohan.dress)             #Green Uniform
print(mohan.__dict__)          #{'dress': 'Green Uniform'}
sohan = Student()
print(sohan.__dict__)          # {} as we have not created any attributes for this object

