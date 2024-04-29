age = input("enter a number")


if int(age) < 18:
  raise Exception("Sorry, no numbers below 18")
else:
  print("you are eligible to vote")


'''enter a number18
you are eligible to vote'''


'''Traceback (most recent call last):
  File "C:\Users\Admin\PycharmProjects\PythonTesting\Day18Exceptions\Demo8.py", line 5, in <module>
    raise Exception("Sorry, no numbers below 18")
Exception: Sorry, no numbers below 18

Process finished with exit code 1'''
