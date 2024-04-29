class NotEligibleToVoteException(Exception) :
  def __init__(self,msg):
    self.msg = msg
    super().__init__(self.msg)

age = input("enter a number")


if int(age) < 18:
  raise NotEligibleToVoteException("Sorry, no numbers below 18")
else:
  print("you are eligible to vote")

  '''enter a number15
Traceback (most recent call last):
  File "C:\Users\Admin\PycharmProjects\PythonTesting\Day18Exceptions\Demo11.py", line 10, in <module>
    raise NotEligibleToVoteException("Sorry, no numbers below 18")
NotEligibleToVoteException: Sorry, no numbers below 18

Process finished with exit code 1
'''



