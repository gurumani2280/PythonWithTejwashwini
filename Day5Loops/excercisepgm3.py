# take radius as user input and print the circumference of the circle
#import math
from typing import Any

r = float(input("Please enter the radius of the circle"))
pie =3.14
print(type(r))
c = 2 * pie* r
print("The circumference of the circle is ",c)