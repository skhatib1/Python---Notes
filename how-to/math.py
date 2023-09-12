####################################
Mathematical Operations
####################################

a = 5
b = 10

# a to the power of b; a^b
answer = 2**3

# How many times a goes into b
answer = b // a

# Get the remainder when dividing
answer = b % a

# Check if number is even
answer = a % 2
if answer == 0:
  print("A is even")
else:
  print("A is odd")

# Numeric value of Bool
# True is 1; False is 0
answer = int(True)
answer = int(False)

''' Math Methods '''
abs(-4) # - Absolute value of -4 (answer: 4)
min(1,2,3,4) # - Returns the minimum value
max(1,2,3,4) # - Returns the maximum value
range(0,100,2) # - Count form 0 - 99, skip by 2)

''' Math Module '''
from math import *
a = sqrt(100) # - the square root of 100
b = ceil(x) # - [x] (i.e., the smallest integer ≥ x)
c = floor(x) # - [x] (i.e., the smallest integer ≥ x)
d = cos(100) # - the cos of value 100
e = sin(100) # - the sin of vlaue 100
f = log(x, base)
e = pi # - 3.14

''' Swap Values'''
x = 1 ; b = 2
x,b = b,x # - Swap values of x and b (x = 2, b = 1)

'''Fractions'''
import fractions
a = fractions.Fraction(2/4) # - Print result as fractions


''' Random Module '''
from random import random
random.randint(0,3)
random.randrange(0,3)
random.uniform(0,1) # - Return random decimal between 0 and 1 (does not incude 0 and 1)
random.shuffle(myList) # - Shuffle order of items in list
random.choice(myList) # - Return one random item from the list



#############################
# Useful Functions
#############################

def isEven(myNumber)
  """Returns True if myNumber is even, False if it is odd"""
  if myNumber % 2 == 0:
      print("The number is even")
      return True
  else:
      print("The number is odd")
      return False
