class SimpleException(Exception) :
  pass

age = input("enter a number")


if int(age) < 18:
  raise SimpleException("Sorry, no numbers below 18")
else:
  print("you are eligible to vote")

'''Traceback (most recent call last):
  File "C:\Users\Admin\PycharmProjects\PythonTesting\Day18Exceptions\Demo10.py", line 8, in <module>
    raise SimpleException("Sorry, no numbers below 18")
SimpleException: Sorry, no numbers below 18

Process finished with exit code 1'''

