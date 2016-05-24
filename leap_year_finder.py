#leap year finder
import math
leap=int(input("find what year is a leap year:"))
if leap % 400 == 0 or leap % 4 ==0:
	print( "%d is a leap year" %leap)
	...
elif leap % 400 != 0 or leap % 4 != 0:
	print("%d is not a leap year" %leap)
	...
else:
	print("number not identified")
	...