#static methods will not access to both instance and class variable

class mathutil :
    @staticmethod
    def getmaxvalue(a,b):
        return max(a,b)

print(mathutil.getmaxvalue(5,4))