class Test:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("object is removed")

P1=Test()
P1=None              #these objects are known as garbage collections
print("program completed")