#Accept a real number x as input and print the greatest integer less than or equal to x on the first line, followed by the smallest integer greater than or equal to x on the second line.
import math
from fractions import Fraction
r = input()
try:
	r = eval(r)
except:
	r = float(r)
if r % 1== 0:
	r = int(r)
	print(r)
	print(r+1)
else:
	t= r - (r%1)
	t = int(t)
	print(t)
	print(t+1)