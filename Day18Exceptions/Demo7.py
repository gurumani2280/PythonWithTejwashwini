age = input("enter a number")


if age < 18:      # TypeError: '<' not supported between instances of 'str' and 'int'
  raise Exception("Sorry, no numbers below zero")