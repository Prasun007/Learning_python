#               METHOD I
me="This is Prasun"
number=50
print("%s "%me)
# a="I am %s %s"%(me,number)# Tuple (me,number) for two variables.
#print(a)
#               METHOD II
a="I am {} {}"
#a="I am {1} {0}"# Variables interchange.
b=a.format(me,number)
print(b)
#               METHOD III
import math
a=f"I am {me} {number} {5*5} {math.factorial(5)}"# We can calculate and use modules inside f strings
print(a)